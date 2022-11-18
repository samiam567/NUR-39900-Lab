
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================
'''
from .GameEngineToolbox import checkType
from math import pi,sin,cos


'''
sends a ray starting from the given position and at the given angle and returns the distance when the passed function is true or the max length is exeeded

params:
startpos - tuple[float] - the position to start the ray at
angle - float - the angle (in degrees)
length - float - the maximum length to probe
function - function - stop when this function returns functionOutput
functionOutput - boolean - stop when the function output equals this
increment - float - how much to increment the probing length each time
'''
def raytrace(startpos,angle,length,function,functionOutput,increment = 1.3):
    checkType(startpos,(tuple),"starting position must be a tuple");
    checkType(startpos[0],(float,int),"start pos must contain numbers");
    checkType(angle,(float,int),"angle must be a number");
    checkType(length,(int,float),"ray length must be a number");
   # checkType(function,(type(raytrace)),"function must be of type function");
    checkType(increment,(float,int),"increment must be a number");

    angle = pi*angle/180; # convert angle to radians
    
    cLength = 0; # the current probe-length for the ray

    # set the position of the ray to the startposition
    x = startpos[0];
    y = startpos[1];

    # while we have not exceeded the length and the function did not return true
    while ( (not (function(x,y) == functionOutput) ) and (cLength < length) ):
        cLength += increment; # increment the length of the ray

        # calculate the pos of the endpoint of the ray
        x = startpos[0] + cLength * cos(angle);
        y = startpos[1] + cLength * sin(angle);
        
    return cLength
    
        








'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
