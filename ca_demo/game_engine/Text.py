
from .GameEngineToolbox import checkType
import pygame
from .Object2D import Object2D

class Text(Object2D):

    def __init__(self,name,xPosition,yPosition,fontFamily="freesansbold.ttf",fontSize=32,color=(0,0,0),highLightColor=(255,255,255)):
        super(Text,self).__init__(name,xPosition,yPosition,1,1);

        self.color = color;

        self.font = pygame.font.Font(fontFamily, int(fontSize))
        
        self.highLightColor = highLightColor;

        self.setText(self.name);

    def setColor(self,color):
        checkType(color,tuple); 
        self.color = color;

    def setText(self,text):
        self.text = self.font.render(text, True, self.color, self.highLightColor );
        self.textRect = self.text.get_rect()
      
        self.textRect.topleft = (self.xPosition-self.xSize/2, self.yPosition-self.ySize/2);

    def paint(self, screen):
        screen.blit(self.text, self.textRect);