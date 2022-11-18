
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================
'''
from .Object2D import Object2D
from .ObjectDraw import ObjectDraw
from .GameEngineToolbox import checkType
from .Sprite import Sprite
from math import atan2, sqrt, sin, cos, pi

# a more advanced sprite that can be painted in the perspective of another object. Basically a simple way of doing cameras
# NOTE: this object will act as a normal Sprite unless you set the camera with setCamera().
# NOTE: if it is a first person game it is customary to set all of the gameobjects' cameras to the RelativeSprite representing the character, INCLUDING setting the camera of the character to itself.
'''
class members:
hasCamera - bool - whether the RelativeSprite has a camera assigned to it. If this is false this object will be painted the same as a normal Sprite.
camera - Object2D - the object that we will paint relative to
zeroXPosition - float - offSets the sprites x position by this amount
zeroYPosition - float - offSets the sprites y position by this amount
zeroRotation - float - offsets the sprites rotation by this amount
displayXPosition - float - the x position that we will display (relative to the camera)
displayYPosition - float - the y position that we will display (relative to the camera)
displayRotation - float - the rotation that we will display (relative to the camera)
'''

class RelativeSprite(Sprite):
    def __init__(self,name,xPosition,yPosition,scaling,imgSource,objectDraw):
        super(RelativeSprite,self).__init__(name,xPosition,yPosition,scaling,imgSource);
        checkType(objectDraw,ObjectDraw,"objectDraw must be an ObjectDraw");

        self.hasCamera = False;
        self.objectDraw = objectDraw;
        self.camera = None;
        self.zeroXPosition = self.objectDraw.screenSizeX/2;
        self.zeroYPosition = self.objectDraw.screenSizeY/2;
        self.zeroRotation = 0;
        self.displayXPosition = xPosition;
        self.displayYPosition = yPosition;
        self.displayRotation = 0;

    # sets the camera of this object to the passed Object2D
    def setCamera(self,camera):
        assert issubclass(camera.__class__, Object2D); # make sure the object we are adding is a child of Object2D
        self.camera = camera;
        self.hasCamera = True;

    # removes the camera from the object so it paints like a normal Sprite
    def removeCamera(self):
        self.camera = None;
        self.hasCamera = False;
        

    # calls the update method of superclasses and updates the displayimage to be in the perspective of the camera
    def update(self):
        if not self.hasCamera:
            super(RelativeSprite,self).update(); # update like a normal Sprite
            if (self.zeroRotation != 0):
                self.rotation += self.zeroRotation;
                super(RelativeSprite,self).updateDisplayImage(); # update the display image with the relative values
                self.rotation -= self.zeroRotation;
        else:
            super(Sprite,self).update(); # call the update method of Object2D, NOT Sprite
            #save current position
            prevRotation = self.rotation;
            self.displayXPosition = self.xPosition;
            self.displayYPosition = self.yPosition;

            cameraPosition = self.camera.getPosition();

      
            #translate relative to the camera
            self.displayXPosition -= cameraPosition[0];
            self.displayYPosition -= cameraPosition[1];



            '''
            rotate around camera
            '''

            #convert to polar
     
            angle = atan2(self.displayYPosition,self.displayXPosition); # the angle of this object relative to the camera
            
            radius = sqrt(self.displayXPosition**2 + self.displayYPosition**2) # thie distance this object is away from the camera

            # rotate the object around the camera <the camera's rotation>
            angle -= pi*self.camera.getRotation()/180;

            # convert back to rectangular and assign to displayPosition
            self.displayXPosition = radius * cos(angle);
            self.displayYPosition = radius * sin(angle);


            self.rotation -= self.camera.getRotation(); # add internal rotation to match camera


            #add zero offsets
            self.rotation += self.zeroRotation;
            self.displayXPosition += self.zeroXPosition;
            self.displayYPosition += self.zeroYPosition;

            #set displayRotation
            self.displayRotation = self.rotation;
            
            
            '''
            update the display image with the relative values
            '''
            super(RelativeSprite,self).updateDisplayImage(); # update the display image with the relative values


            '''
            reset rotation back to where it was before
            '''
            self.rotation = prevRotation;
            # we don't have to reset position since we used displayPosition rather than directly changing the object's position


    #paint relative to the camera
    def paint(self,screen):
        if self.hasCamera:
            # if we have a camera paint using the relative values
            screen.blit(self.displayImg,[self.displayXPosition-self.showSizeX/2, self.displayYPosition-self.showSizeY/2]);
        else:
            # otherwise just use Sprite's paint method
            super(RelativeSprite,self).paint(screen);

    # set the zero position of the relativeSprite
    def setZeroPosition(self,zeroX,zeroY):
        checkType(zeroX,(int,float),"zero position must be a number");
        checkType(zeroY,(int,float),"zero position must be a number");
        self.zeroXPosition = zeroX;
        self.zeroYPosiiton = zeroY;

    #set the zero rotation of the relativeSprite
    def setZeroRotation(self,zeroRot):
        checkType(zeroRot,(int,float),"zeroRotation must be a number");
        self.zeroRotation = zeroRot;
        

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
