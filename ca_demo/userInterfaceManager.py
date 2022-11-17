


from IAC_Button import IAC_Button
from IAC_textBox_Button import IAC_textBox_Button
from game_engine.ObjectDraw import ObjectDraw
from game_engine.Text import Text
from game_engine.Sprite import Sprite
import time
import subprocess
from math import sqrt

colorRed = (255,0,0);
colorGreen = (0,255,0);

screenSplitText = 0.25;
screenSplitButton = 0.9;




def sendCommand(commandStr, shell=True):
    subprocess.run(commandStr, shell=shell);

def createButtons(buttons, objectDraw):
    xStep = objectDraw.screenSizeX / len(buttons);
    
    multFromBtm = 1-screenSplitButton;

    screenSizeY = objectDraw.screenSizeY;
    
    i = 0;
    for key in buttons:
        newBtn = IAC_Button(key, sendCommand,objectDraw, i * xStep + xStep/2 , screenSizeY-screenSizeY*multFromBtm,xSize=xStep,ySize=screenSizeY*multFromBtm, params=buttons[key]);
        objectDraw.add(newBtn);
        i += 1;


class TextUpdater():
    def __init__(self, text, convertMsgToValueFunc, valueRange = (-1000000000000000,10000000000000)):
        self.text = text;
        self.valueRange = valueRange
        self.convertMsgToValue = convertMsgToValueFunc;
    def subFunction(self,msg):
        value = self.convertMsgToValue(msg);
        self.text.setText(self.text.name + ": " + str(value));
        if (float(value) > self.valueRange[0] and float(value) < self.valueRange[1]):
            self.text.setColor(colorGreen);
        else:
            self.text.setColor(colorRed);


def createTopicStatuses(topics,objectDraw):

    # the list of callback functions for the text objects
    subFuncs = [];

    # figure out spacing and fontsize
    yStep = objectDraw.screenSizeY*screenSplitText // (1+len(topics));
    fontSize = 1.0 * yStep;

    # create the text objects
    i = 0;
    for topicName in topics:
        
        text1 = Text(topicName,screenSizeX*0.5-10*fontSize,(5+fontSize) * i + fontSize,fontSize=fontSize,highLightColor=(10,10,10));
        objectDraw.add(text1); # add to object draw to be rendered
        
        # create object to control the color of the text field with the passed function to convert the msg to a value
        textUpdate = TextUpdater(text1,valueRange=topics[topicName][0], convertMsgToValueFunc=topics[topicName][1]);

        # append the subscription callback function
        subFuncs.append(textUpdate.subFunction);
    
        i += 1;

    return subFuncs;







# define params and make objectDraw

screenScale = 1;
screenSizeX = int(1000 * screenScale);
screenSizeY = int(500 * screenScale);

diagonal = sqrt(screenSizeY**2 + screenSizeX**2);

objectDraw = ObjectDraw(screenSizeX,screenSizeY,frameCaption="Coding to prevent coding");


def createUI(buttonsDict, textDict):
    # create background image
    background = Sprite("backgroundlogo",screenSizeX/2,screenSizeY*0.45,scaling=diagonal/1000,imgSource="./assets/Blackandgoldlogo.png");
    objectDraw.setBackgroundColor((0,0,0));
    objectDraw.add(background);






    # create pointless add-ons to make it look cooler
    hologram1 = Sprite("hologram_rotator_1", screenSizeX*0.9,screenSizeY*0.7,diagonal/9000,"./assets/hologram rotator.png");
    hologram1.setAngularVelocity(1);
    objectDraw.add(hologram1);

    hologram2 = Sprite("hologram_rotator_2", screenSizeX*0.07,screenSizeY*0.17,diagonal/10000,"./assets/hologram_radar.jpg");
    hologram2.setAngularVelocity(-1.7);
    objectDraw.add(hologram2);


    # create buttons and text messages


    

    createButtons(buttonsDict,objectDraw);





    # start the engine
    objectDraw.start();

    return objectDraw;






if __name__ == "__main__":

    def msg_to_val(msg):
        return msg.data;

    # title, command
    buttonsDict = {
        "Am I gonna die?": ("echo 'command send ct11'",""),
    };

    # topicname, (lower, upper)
    textDict = {
        "novatel/bottom/bestpos" : ((10,1000),msg_to_val),
        "raptor_dbw_interface/imu" : ((1,100),msg_to_val),
        "raptor_dbw_interface/ctstate": ((0,20),msg_to_val),
        "raptor_dbw_interface/wheel_speed_report": ((10,11),msg_to_val),
        "raptor_dbw_interface/imu_error": ((10,500),msg_to_val),
        "raptor_dbw_interface/gps_covariance": ((100,300),msg_to_val)
    }


    subFuncs = createUI(buttonsDict,textDict)[0];


    # run the engine
    class msg():
        def __init__(self,data):
            self.data = data;

    import random

    i = 1;
    while(True):
        i+=1;
        
        
        for fun in subFuncs:
        
            msg1 = msg(random.randint(0,100));
            fun(msg1);
            

        objectDraw.run();
        time.sleep(0.1);

