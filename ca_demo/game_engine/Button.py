
'''
===============================================================================
    Project:        Python Game Engine
	Author:         Alec Pannunzio, afpannun@purdue.edu
===============================================================================
'''


from typing import TextIO
from .GameEngineToolbox import checkType
from .GameObject import GameObject
from .Object2D import Object2D


from pygame_button import Button as BT

default_button_style = {
    "hover_color": (0,255,255),
    "clicked_color": (0,255,0),
    "clicked_font_color": (0,0,0),
    "hover_font_color": (0,0,0),
  #  "hover_sound": pg.mixer.Sound("blipshort1.wav"),
}

class Button(Object2D):

    def event_func(self):
        self.onButtonClick();
        self.func_to_call(self.funcParams);

    def __init__(self,name,func_to_call,objectDraw, xPosition, yPosition,xSize,ySize, text=False, style=default_button_style,params=(),color=(100,100,100)):
        super(Button,self).__init__(name,xPosition,yPosition,xSize,ySize);
        #checkType(event_func,function.__class__,"event function must be of type function");
        checkType(xPosition,(int,float));
        checkType(yPosition,(int,float));
        checkType(xSize,(int,float));
        checkType(ySize,(int,float));
        
        # if we haven't been passed button text, just use the name of this object
        if (not text):
            self.text = name;
        else:
            self.text = text;

        self.func_to_call = func_to_call;
        self.funcParams = params;
        self.screen_rect = objectDraw.screen.get_rect()

        self.color = color;
        
        self.style = style;


        self.updateButtonParams();
        

    # may be overriden by child classes
    def onButtonClick(self):
        pass;  


    def updateButtonParams(self):
        self.button = BT((0, 0, self.xSize, self.ySize), self.color, self.event_func, text=self.text, **self.style);

    def setColor(self,color):
        self.color = color;
        self.updateButtonParams();
        

  
    def paint(self, screen):
        self.button.rect.center = (self.xPosition, self.yPosition);
        self.button.update(screen);
