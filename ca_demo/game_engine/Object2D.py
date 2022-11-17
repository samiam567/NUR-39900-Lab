'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================

'''
from .GameObject import GameObject
from .GameEngineToolbox import checkType



# Object2D is a template for an object that can be transformed around the screen
'''
class members:
xPosition - float - the position of the center of this object on the x axis
yPosition - float - the position of the center of this object the y axis
xSpeed - float - the speed of the object in the x direction
ySpeed - float - the speed of the object in the y direction
xAcceleration - float - the acceleration of the object in the x direction
yAcceleration - float - the acceleration of the object in the y direction
rotation - float - the rotation of this object (in radians)
angularVelocity - float - the speed at which the object is rotating
xSize - int - the size of this object in the x dimension
ySize - int - the size of this object in the y dimension
'''

class Object2D(GameObject):
    # initialize the object
    def __init__(self,name,xPosition,yPosition,xSize,ySize):
        super(Object2D,self).__init__(name);

        #check types
        checkType(xPosition,(int,float),"xPosition must be an number");
        checkType(yPosition,(int,float),"yPosition must be an number");
        checkType(xSize,(int,float),"xSize must be an number");
        checkType(ySize,(int,float),"ySize must be an number");

        # set the passed parameters to their respective class members
        self.xPosition = xPosition;
        self.yPosition = yPosition;
        self.xSize = xSize;
        self.ySize = ySize;

        # initialize the rest of the class members to zero
        self.xSpeed = 0;
        self.ySpeed = 0;
        self.xAcceleration = 0;
        self.yAcceleration = 0;
        self.rotation = 0.0;
        self.angularVelocity = 0;
        


    # updates the object values. is call repetively by the update loop
    def update(self):
        super(Object2D,self).update();
        self.xPosition += self.xSpeed;
        self.yPosition += self.ySpeed;

        self.xSpeed += self.xAcceleration;
        self.ySpeed += self.yAcceleration;

        self.rotation += self.angularVelocity;


    # sets the position of the object
    def setPosition(self,xPos, yPos):
        checkType(xPos,(int,float),"xPosition must be an int");
        checkType(yPos,(int,float),"yPosition must be an int");
        self.xPosition = xPos;
        self.yPosition = yPos;

    # sets the position of the object
    def setPosition(self, position):
        checkType(position,tuple,"position must be a tuple");
        self.xPosition = position[0];
        self.yPosition = position[1];


    # sets the speed of the object
    def setSpeed(self,xSpeed,ySpeed):
        checkType(xSpeed,(int,float),"xSpeed must be a number");
        checkType(ySpeed,(int,float),"ySpeed must be a number");
        self.xSpeed = xSpeed;
        self.ySpeed = ySpeed;

    # sets the speed of the object
    def setSpeed(self,speed):
        checkType(speed,tuple,"speed must be an tuple");
        self.xSpeed = speed[0];
        self.ySpeed = speed[1];


    # sets the acceleration of the object
    def setAcceleration(self,xAccel,yAccel):
        checkType(xAccel,(int,float),"xAcceleration must be a number");
        checkType(yAccel,(int,float),"yAcceleration must be a number");
        self.xAcceleration = xAccel;
        self.yAcceleration = yAccel;

    # sets the acceleration of the object
    def setAcceleration(self,acceleration):
        checkType(acceleration,tuple,"acceleration must be an tuple");
        self.xAcceleration = acceleration[0];
        self.yAcceleration = acceleration[1];

    #sets the rotation of the object
    def setRotation(self,rot):
        checkType(rot,(int,float),"rotation must be a number");
        self.rotation = rot;

    # sets the angular velocity of the object
    def setAngularVelocity(self,angV):
        checkType(angV,(int,float),"angularVelocity must be a number");
        self.angularVelocity = angV;

    # returns a list containing the [xPosition, yPosition]
    def getPosition(self):
        return (self.xPosition,self.yPosition);

    # returns a list containing the [xSpeed, ySpeed]
    def getSpeed(self):
        return (self.xSpeed, self.ySpeed);

    # returns a list containing the [xAcceleration, yAcceleration]
    def getAcceleration(self):
        return (self.xAcceleration, self.yAcceleration);

    # returns the rotation
    def getRotation(self):
        return self.rotation;

    # returns the angular velocity
    def getAngularVelocity(self):
        return self.angularVelocity;


# tests this class
def testObject2D():
    bob = Object2D("bob",0,0,10,10);
    print(bob.getName());
    bob.setSpeed(1,2);
    bob.setAcceleration(2,1);
    bob.update();
    bob.update();
    print(bob.getPosition());
    print(bob.getSpeed());



'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
