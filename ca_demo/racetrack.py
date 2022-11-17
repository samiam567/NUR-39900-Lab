from .game_engine.Sprite import Sprite
from .game_engine.RelativeSprite import RelativeSprite
import pymap3d as p3d

import os

'''
Finding coords for tracks:
https://earth.google.com/web/search/Indianapolis+Motor+Speedway,+West+16th+Street,+Indianapolis,+IN/@39.79749239,-86.23331699,219.1043837a,1169.72532299d,35y,0h,0t,0r/data=CigiJgokCVa07OC2uz1AEZG8YtDoWyHAGRtBYOW4H0XAIUV1CJoNeGPA
https://gps-coordinates.org/coordinate-converter.php
'''

class Racetrack(RelativeSprite):
    def __init__(self,objectDraw,useIMS=True,scaleMultiplier=1):


        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;


        picSrc = "";
        if (useIMS):
            #picSrc = os.path.join(get_package_share_directory('visualization'), "visualization/assets/IMS.png");
            
            picSrc = "/home/apun1/on-vehicle/src/extras/visualization/visualization/assets/IMS.png";
            # lat and long at the upper left and bottom right corners of the image
            self.trackRefLat = 39.802612; # 39 48 09 N
            self.trackRefLong = -86.241360;# 86 14 29 W
            trackRefLatEnd = 39.787514; # 39 48 09 N
            trackRefLongEnd = -86.226993;# 86 14 29 W

            # pixel dimensions of the image
            self.picDimX = 1955.0; #pixels
            self.picDimY = 2682.0; # pixels



        else:

            #picSrc = os.path.join(get_package_share_directory('gps_visualization'),"assets/LOR.png")
            picSrc = "/home/apun1/on-vehicle/src/extras/visualization/visualization/assets/LOR.png";
            
            # lat and long at the upper left and bottom right corners of the image
            self.trackRefLat = 39.814556; # 39 48 09 N
            self.trackRefLong = -86.342911;# 86 14 29 W
            trackRefLatEnd = 39.810532; # 39 48 09 N
            trackRefLongEnd = -86.339162;# 86 14 29 W

            # pixel dimensions of the image
            self.picDimX = 1633.0; #pixels
            self.picDimY = 2282.0; # pixels

        # scales the image by this factor
        self.scale = scaleMultiplier*float(screenXSize)/self.picDimX;

        #print("scale:",self.scale)

        # find the dimensions of the track in ned units
        self.real_trackYWidth, self.real_trackXWidth,z = p3d.geodetic2ned(trackRefLatEnd, trackRefLongEnd,0,self.trackRefLat,self.trackRefLong,0);
        self.real_trackXWidth = abs(self.real_trackXWidth);
        self.real_trackYWidth = abs(self.real_trackYWidth);

        #print("real trackwidth: ", self.real_trackXWidth, self.real_trackYWidth);




        super(Racetrack,self).__init__("racetrack",objectDraw.screenSizeX/2,objectDraw.screenSizeY/2,self.scale,picSrc,objectDraw=objectDraw);

        objectDraw.add(self);


    def getTrackRelativePosition(self,lat, long, alt=0):

        #print("lat,long,alt: ", lat,long,alt);

        y_real,x_real,z = p3d.geodetic2ned(lat,long,alt,self.trackRefLat, self.trackRefLong,0); # lat,long,alt -> north,east,down wrt trackRef
        y_real = -y_real; # y is negative because in the engine south is a positive y

        #print("x,y real: ",x_real,y_real);

        conversion_x = self.picDimX*self.scale/self.real_trackXWidth;
        conversion_y = self.picDimY*self.scale/self.real_trackYWidth;

        #print("conv x,y : ",conversion_x, conversion_y);
        x = (x_real)*conversion_x;
        y = (y_real)*conversion_y;

        #print("x,y: ", x, y);


        track_position = self.getPosition();

        #print("track size ", self.xSize, self.ySize);

        #print("racetrack pos: ", track_position);
        x_rel = x - self.xSize/2.0 + track_position[0];
        y_rel = y - self.ySize/2.0 + track_position[1];

        #print("x_rel, y_rel: ", x_rel, y_rel);

        return x_rel,y_rel;
