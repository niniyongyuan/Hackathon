# HackCMU 2013
# Weiqi Cai, Megan Chen, Lina Li, Teng Zhang

from Tkinter import *

###########################################
# Game class
###########################################

class mainGame(object):
    # Override these methods when creating your own animation
    def keyPressed(self, event):
        if (event.keysym == "a" or event.keysym == "Left"):
            self.centerX -= self.speed
            self.faceLeft = True # use this state for char dir. facing
        if (event.keysym == "d" or event.keysym == "Right"):
            self.centerX += self.speed
            self.faceLeft = False
        if (event.keysym == "w" or event.keysym == "Up"):
            self.centerY -= self.speed
            self.jumping = True
        if (event.keysym == "p"):
            self.isPaused = not self.isPaused
    def timerFired(self): pass
    def init(self):
        self.isPaused = False
        self.jumping = False
        self.faceLeft = False
    def redrawAll(self): pass
    def run(self, width=600, height=400):
        # create the root and the canvas
        root = Tk()
        root.wm_title("Mission Gravimpossible")
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()
        # set up events
        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll()
        def mousePressedWrapper(event):
            self.mousePressed(event)
            redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)
        # set up timerFired events
        self.timerFiredDelay = 250 # milliseconds
        def timerFiredWrapper():
            self.timerFired()
            redrawAllWrapper()
            # pause, then call timerFired again
            self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
        # init and get timerFired running
        self.init()
        timerFiredWrapper()
        # and launch the app
        root.mainloop()

game = mainGame()
game.run()

