from game_engine.Button import Button





class IAC_Button(Button):

    def __init__(self, name, func_to_call, objectDraw, xPosition, yPosition, xSize, ySize, params):
        super().__init__(name, func_to_call, objectDraw, xPosition, yPosition, xSize, ySize, params=params, color=(150,0,0));

        self.IS_ON = False;

    def onButtonClick(self):
        if (not self.IS_ON):
            self.color = (0,150,0);
            self.IS_ON = True;
        else:
            self.IS_ON = False;
            self.color = (150,0,0);
        self.updateButtonParams();
        return super().onButtonClick();

    def event_func(self):
        self.onButtonClick();

        if (self.IS_ON):
            self.func_to_call(self.funcParams[0]);
        else:
            self.func_to_call(self.funcParams[1]);

        