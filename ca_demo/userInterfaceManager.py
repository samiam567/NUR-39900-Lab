# import python code
import time
import subprocess
from math import sqrt
from random import random

# import graphics elements
from CA_Button import CA_Button
from game_engine.ObjectDraw import ObjectDraw
from game_engine.Text import Text
from game_engine.Sprite import Sprite

# import neural net
from neural_net.ca_neural_net import neuralnet_predict

colorRed = (255,0,0);
colorGreen = (0,255,0);

screenSplitText = 0.25;
screenSplitButton = 0.9;



CA_text = None;


def get_prediction(input):

    positive_answers = ["You will live... for now", "You may actually make it home", "you're luckier than the last patient was"];
    negative_answers = ["Obesity is a risk factor...","You have 5 to live...4...3...2..","student 8 will paint your gravestone","I hope you've made your Will", "Do you have funeral plans yet?", "How old are you again?", "Well you were a high risk patient...", "honestly it's a skill issue"];


    # call neural net
    prediction = neuralnet_predict(random.random());

    # update some text on the screen
    if (prediction > 0.5):
        response = negative_answers[(int) (random.random() * len(negative_answers))];
        CA_text.setText(response);
    else:
        response = positive_answers[(int) (random.random() * len(positive_answers))];
        CA_text.setText(response);

    prevPos = CA_text.getPosition();
    CA_text.setPosition((screenSizeX/2-5*len(response),prevPos[1]));


# define params and make objectDraw
screenScale = 1;
screenSizeX = int(1000 * screenScale);
screenSizeY = int(500 * screenScale);

diagonal = sqrt(screenSizeY**2 + screenSizeX**2);

objectDraw = ObjectDraw(screenSizeX,screenSizeY,frameCaption="Heart Attack Shack - Coding to prevent coding");





# add all the elements to the object draw

# create background image
background = Sprite("backgroundlogo",screenSizeX/2,screenSizeY*0.45,scaling=diagonal/1000,imgSource="./assets/ekg_image.jpeg");
objectDraw.setBackgroundColor((0,0,0));
objectDraw.add(background);


# create pointless add-ons to make it look cooler
hologram1 = Sprite("hologram_rotator_1", screenSizeX*0.9,screenSizeY*0.7,diagonal/9000,"./assets/heart.png");
hologram1.setAngularVelocity(1);
objectDraw.add(hologram1);

hologram2 = Sprite("hologram_rotator_2", screenSizeX*0.07,screenSizeY*0.17,diagonal/10000,"./assets/heart.png");
hologram2.setAngularVelocity(-1.7);
objectDraw.add(hologram2);


# create output text
fontSize = 30;
CA_text = Text("Are you going to have CA??",screenSizeX*0.35,screenSizeY*0.5,fontSize=fontSize,highLightColor=(255,255,255));
CA_text.color = (0,0,0);
CA_text.highLightColor = (255,255,255);
objectDraw.add(CA_text); # add to object draw to be rendered

bYSize = 40;
button = CA_Button("Ask Predict-O-Bot 9000!", get_prediction,objectDraw, screenSizeX/2, screenSizeY-bYSize*1.5,xSize=screenSizeX/2,ySize=bYSize, params="none");

objectDraw.add(button);

objectDraw.start();

# run the engine
class msg():
    def __init__(self,data):
        self.data = data;

import random

i = 1;
while(True):
    i+=1;

    objectDraw.run();
    time.sleep(0.1);

