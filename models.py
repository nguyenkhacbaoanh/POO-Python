import json
import math

class Agent:

    def __init__(self, position, **agent_attrs):
        #add a parameter position in class Agent
        self.position = position
        # a loop to set all attributes from JSON to class
        for attr_name, attr_value in agent_attrs.items():
            # set attribute
            setattr(self, attr_name, attr_value)

#Create new class Position
class Position:
    
    #initialization
    def __init__(self, latitude_degrees, longitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees

    #to convert from latitude degree to radian
    #use method property to set this method like attribute, it means that this method don't need ()
    @property
    def latitude(self):
        return (self.latitude_degrees * math.pi / 180)

    @property
    def longitude(self):
        return (self.longitude_degrees * math.pi / 180)

# create class Zone:
class Zone:

    # a range for longitude degree, latitude degree and theirs steps
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    WIDTH_DEGREES = 1
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    HEIGHT_DEGREES = 1

    ZONES = []    

    #declaration parameters of class Zone
    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []
    
    @property
    def population(self):
        return (len(self.inhabitants))

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)
    
    def contains(self, position): #to verify whether ours inhabitants in ours zones or not 
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(self.corner1.latitude, self.corner2.latitude)
    
    @classmethod
    def find_zone_that_contains(cls, position): #to find zone that include positions of ours inhabitants
        if not cls.ZONES:
            cls.initialize_zones()

    #computer the index in the ZONES array that contains a given position
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index
    
    # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone
    
    
    #because in loop, we call class ZONE, we have been stuck by a loop illimited
    #use classmethod to use this method in your class, don't need a instance to use it
    @classmethod #we have change "self" to "cls" adcording to convention
    def initialize_zones(cls): #we initialize our zone by a method:
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(latitude, longitude)
                top_right_corner = Position(latitude + cls.HEIGHT_DEGREES, longitude + cls.WIDTH_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)

def main():
    #a loop to set attributes from list of 100k agents
    for agent_attributes in json.load(open('agents-100k.json')):
        # use method pop in dist to make instance and delete this key:value in dist
        #because we don't need anymore
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        position = Position(latitude, longitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        print("Zone population: ", zone.population)

main()