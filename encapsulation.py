# exemple following, i uses a cafe's machine to prove how we
# use an encapsulation in ours programmes

# Encapsulation is a way to associate methods of class and
# when it's executed, some implicit method have run in internal

# With cafe machine, it have been created by a lot of process
# By our view, it have a button on its face to make a cup of coffee
# when we presse it, some implicit process have implemented like 
# to boil water, this process called private method, we can't execute it from external class

# In encapsulation: we have 3 method:
#       - protected (start coffe machin)
#       - private (boil water)
#       - public (make coffe)
class CoffeMachine:

    # we put an attribute to create a condition specify in method start machine
    LEVELS_WATER = 100 # have enough water in machine

    def _start_machine(self): # add one underscore before method protected
        #protected method
        if self.LEVELS_WATER >= 20:
            return True
        else:
            return False
            print("Not enough water! Please add water!")
            
    def __boils_water(self): # add two underscores before method private
        #private method
        print("Soiling...")

    def make_coffe(self):
        #public method
        if self._start_machine():
            self.LEVELS_WATER -= 20
            self.__boils_water()
            print("Yum, good coffe!")

cup_coffee = CoffeMachine()
# for cup in range(5): # a loop permit me to make 5 cup of coffee
#     cup_coffee.make_coffe()
print(cup_coffee._start_machine()) # True
cup_coffee.make_coffe()            # Soiling...
                                   # Yum, good coffe
# cup_coffee.__boils_water()         # error: "CoffeMachine" has no attribute '__boils_water'

# to resolve this error, we add '_NameofClass' before method private:
cup_coffee._CoffeMachine__boils_water()


# Output:
# Soiling...
# Yum, good coffe!
# Soiling...
# Yum, good coffe!
# Soiling...
# Yum, good coffe!
# Soiling...
# Yum, good coffe!
# Soiling...
# Yum, good coffe!