
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================
'''

# an object that can be used in the game engine. has very general properties

'''
class members
name - string - the name of the GameObject
'''
from .GameEngineToolbox import checkType;

class GameObject():
    #initialize the GameObject
    def __init__(self,name): 
        self.name = str(name); #store the name as one of our class members

    # returns the gameObject's name
    def getName(self):
        return self.name;

    # this is called by the engine thread and child classes will override this
    def update(self):
        pass;

    # this is called by the engine thread and child classes will override this
    def paint(self,screen):
        print(self.getName(), "has no overridden paint method");
        pass;


# tests this class
def testGameObject():
    bob = GameObject("bob");
    print(bob.getName());
    
    badboi = GameObject(69);
    print(badboi.getName());



'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
