# HackCMU 2013
# Weiqi Cai, Megan Chen, Lina Li, Teng Zhang

from Tkinter import *
import Person

###########################################
# Game class
###########################################

class mainGame(object):
    # Override these methods when creating your own animation
    def keyPressed(self, event):
        if (event.keysym == "a" or event.keysym == "Left"):
            person.centerX -= person.speed
            person.faceLeft = True # use this state for char dir. facing
        if (event.keysym == "d" or event.keysym == "Right"):
            person.centerX += person.speed
            person.faceLeft = False
        if (event.keysym == "w" or event.keysym == "Up"):
            person.centerY -= person.speed
            person.jumping = True
        if (event.keysym == "p"):
            self.isPaused = not self.isPaused
    def timerFired(self): pass
    def init(self, canvas):
        self.isPaused = False
        self.person = Person(canvas)
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
        self.init(canvas)
        timerFiredWrapper()
        # and launch the app
        root.mainloop()

game = mainGame()
game.run()
