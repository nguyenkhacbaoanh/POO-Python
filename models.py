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

def read_json(source):
    source = str(source)
    with open(source) as f:
        data = json.load(f)
    return data

def main():
    #a loop to set attributes from list of 100k agents
    for agent_attributes in read_json('agents-100k.json'):
        # use method pop in dist to make instance and delete this key:value in dist
        #because we don't need anymore
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        position = Position(latitude, longitude)
        agent = Agent(position, **agent_attributes)
        print(agent.position.latitude)

main()