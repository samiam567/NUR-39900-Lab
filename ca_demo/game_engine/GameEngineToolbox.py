
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================
'''
# a toolbox full of useful functions for the game engine




#checks that the passed variable is of the passed required type or types. Returns True if it is, false otherwise
def checkType(variable, requiredTypes, errorMessage = "Incorrect type", raiseError = True):
    rightType = False;

    if type(requiredTypes) is tuple:
        for requiredType in requiredTypes:
            if (type(variable) is requiredType):
                rightType = True;

        if (raiseError):
            if not rightType:
                raise TypeError(errorMessage);
            
        return rightType;
    else:
        if not (type(variable) is requiredTypes):
            if (raiseError):
                raise TypeError(errorMessage);
            return False;
        else:
            return True;

# will make all objects bounce off the borders of the screen
def border_bounce(objectDraw):
    for current_object in objectDraw.objects:
       
        if (current_object.getPosition()[0] > objectDraw.screenSizeX-current_object.xSize/2):
            current_object.setSpeed((-1 * abs(current_object.getSpeed()[0]),current_object.getSpeed()[1]));
            
        if (current_object.getPosition()[1] < current_object.ySize/2):
            current_object.setSpeed((current_object.getSpeed()[0],abs(current_object.getSpeed()[1])));

        if (current_object.getPosition()[0] < current_object.xSize/2):
            current_object.setSpeed((abs(current_object.getSpeed()[0]),current_object.getSpeed()[1]));
            
        if (current_object.getPosition()[1] > objectDraw.screenSizeY-current_object.ySize/2):
            current_object.setSpeed((current_object.getSpeed()[0],-1 * abs(current_object.getSpeed()[1])));





'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
