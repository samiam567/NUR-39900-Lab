
from .car_visual import Car_visual
from .game_engine.ObjectDraw import ObjectDraw
from .racetrack import Racetrack

class IAC_visualization_frame():

    def __init__(self,first_person=True,useIMS=True):
        screenScale = 1;
        screenXSize = int(screenScale*700);
        screenYSize = int(screenScale*1000);
        self.objectDraw = ObjectDraw(screenXSize, screenYSize);


        self.objectDraw.setBackgroundColor((0,255,0));



        if (first_person):
            self.car_visual = Car_visual(self.objectDraw,scaleMultiplier=0.4);
            self.racetrack = Racetrack(self.objectDraw, useIMS=useIMS,scaleMultiplier=7); # True for IMS, False for LOR

            self.racetrack.setCamera(self.car_visual);
            self.car_visual.setCamera(self.car_visual);

            self.objectDraw.add(self.car_visual);
        else:
            self.car_visual = Car_visual(self.objectDraw,scaleMultiplier=0.3);
            self.racetrack = Racetrack(self.objectDraw, useIMS=useIMS); # True for IMS, False for LOR
            self.objectDraw.add(self.car_visual);


        # start the simulation
        self.objectDraw.start();

    def run(self):
        self.objectDraw.run();

    def updateCarPos(self,lat, long):
        self.car_visual.setPosition(self.racetrack.getTrackRelativePosition(lat,long));

    def updateCarHeading(self,head):
        self.car_visual.setRotation(head);
