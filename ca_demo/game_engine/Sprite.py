
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
from .GameEngineToolbox import checkType;
from math import sin, cos, pi, atan, tan
import pygame



# an image that can be moved and rotated
'''
class members:
imgSource - string - the source of the image
img - pygame.Surface - the image object
displayImg - pygame.Surface - the transformed image object ready to be displayed
showSizeX - int - the size the image is transformed to in the x dimension. (when the image rotates the corners would stick out so we have to allow a bigger box for the picture to fit in in the transformation)
showSizeY - int - the size the image is transformed to in the y dimension. (when the image rotates the corners would stick out so we have to allow a bigger box for the picture to fit in in the transformation)
imgScale - float - how many times bigger this surface is than the original image
'''

class Sprite(Object2D):
    def __init__(self,name,xPosition,yPosition,scaling,imgSource):
        checkType(scaling,(int,float),"the scaling factor must be a int or float");
        
        
        #calculate the size of the image
        self.img = pygame.image.load(imgSource).convert(); # load the image from the imgSource
        self.xSize = scaling * self.img.get_width();
        self.ySize = scaling * self.img.get_height();
        
        super(Sprite,self).__init__(name,xPosition,yPosition,self.xSize,self.ySize);
        
        self.img.set_colorkey((0,0,0)); # set the colorkey of the image to black
        
        self.displayImg = self.img; #initialize displayImg

        # initialize some class members
        self.showSizeX = self.xSize;
        self.showSizeY = self.ySize;
        self.imgScale = scaling;
    
    


    # updates the sprite and readies it for rendering  
    def updateDisplayImage(self):
        # rotate the image to the correct rotation
        self.displayImg = pygame.transform.rotate(self.img,-self.rotation);


        '''
        scale the image
        (compensate for the corners sticking out from the bounding box by scaling the image that much larger)
        '''

        # calculate how far away from the center the corners would be
        cornerAngle = atan(self.ySize/self.xSize); 

        cornerDist = ((self.ySize/2)**2 + (self.xSize/2)**2)**0.5; #the length from the center of the rectangle to the corner. Serves as the "hypotenuse"

        # X dimension
        showSizeX1Multi = abs(cos(cornerAngle + pi*(self.rotation)/180)); #corner @ 45 degrees if unrotated
        showSizeX2Multi = abs(cos(-cornerAngle + pi*(self.rotation)/180)); #corner @ -45 degrees if unrotated

        #use the larger of the two
        if (showSizeX1Multi > showSizeX2Multi):
            showSizeXMulti = showSizeX1Multi;
        else:
             showSizeXMulti = showSizeX2Multi;

        # Y dimension
        showSizeY1Multi = abs(sin(cornerAngle + pi*(self.rotation)/180)); #corner @ 45 degrees if unrotated
        showSizeY2Multi = abs(sin(-cornerAngle + pi*(self.rotation)/180)); #corner @ -45 degrees if unrotated

        #use the larger of the two
        if (showSizeY1Multi > showSizeY2Multi):
            showSizeYMulti = showSizeY1Multi;
        else:
            showSizeYMulti = showSizeY2Multi;


        #calculate the size we should scale the picture to
        self.showSizeX = int(2*cornerDist*showSizeXMulti);
        self.showSizeY = int(2*cornerDist*showSizeYMulti);

        
        self.displayImg = pygame.transform.scale(self.displayImg, (self.showSizeX,self.showSizeY));
    
    #updates this Sprite
    def update(self):
        super(Sprite,self).update(); # call the update of the parent class
        self.updateDisplayImage(); 
        
        
    #rotates the picture, but not the actual sprite object
    def rotatePicture(self,angle):
        self.img = pygame.transform.rotate(self.img,angle);
        self.xSize = self.imgScale * self.img.get_width();
        self.ySize = self.imgScale * self.img.get_height();

    def paint(self,screen):
        # paint the Sprite, adjusting so that the xPosition,yPosition are the coordinates of the center
        screen.blit(self.displayImg,[self.xPosition-self.showSizeX/2, self.yPosition-self.showSizeY/2]);








'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
