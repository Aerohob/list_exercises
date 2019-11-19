#Classes are for:
#bundling related data (like a dictionary)
# with the functions that modify the data

#Encapsulation - hiding the details about how something is done (usually inside of methods)
#Encapsulation, alternate definition - bundling related data along with functions that use and modify that data

#Inheritance- making specialized classes based on other classes

#Polymorphism - methods can interact with lots of different kinds of objects, and it doesn't care what class created it

#Composition - not stuffing everything into a single class. Instead make classes that help other classes
#Create specialized objects that cooperate with each other. 

from CatInheritence import Cat
from random import randint

class CuddlyCat(Cat):
    def __init__ (self, new_name): # could be (self, new_name, friendless, etc)
        super().__init__(new_name, 0.99, 50, 5)
    
    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            #As long as 'whom' has a .name and a .happiness
            #The cuddle method can do its work
            #When a method can interact with many different kids of an object
            # this is called Polymorphism
            print(f"I cuddle you, {whom.name}!")
            whom.happiness *= self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")
        
artemis = CuddlyCat('Artie')