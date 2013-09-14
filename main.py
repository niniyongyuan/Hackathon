# HackCMU 2013
# Weiqi Cai, Megan Chen, Lina Li, Teng Zhang

from Tkinter import *

class Person(object):
    def __init__(self, canvas):
        self.radius = 10
        self.canvas = canvas
        #magic number need to be changed to canvas.height-size
        self.centerX = 10
        self.centerY = 100
        self.iscollide = False
        self.floatspeedx = 0
        self.floatspeedy = 0
        self.speedX = 5
        self.speedY = 0
        self.jumping = False
        self.heading = True

    def drawPerson(self, canvas):
        left = self.centerX - self.radius
        right = self.centerX + self.radius
        top = self.centerY - self.radius
        bottom = self.centerY + self.radius
        #change it to load the person
        canvas.create_oval(left, top, right, bottom, fill="red")

    def run(self):
        if self.heading:
            self.centerX += self.speed
        else: self.centerX -= self.speed


    def jump(self):
        self.centerY += self.speedY
        self.speedY++


###########################################
# Game class
###########################################

class mainGame(object):
    def keyPressed(self, event):
        if (event.keysym == "a" or event.keysym == "Left"):
            self.canvas.data.person.heading = False
            self.canvas.data.person.run()
            #redrawAll()# use this state for char dir. facing
        if (event.keysym == "d" or event.keysym == "Right"):
            self.canvas.data.person.heading = True
            self.canvas.data.person.run()   
        if (event.keysym == "w" or event.keysym == "Up"):
            self.canvas.data.person.jumping = True
            self.jumpSpeed = -5
            self.canvas.data.person.jump()
        if (event.keysym == "p"):
            self.isPaused = not self.isPaused
    # Override these methods when creating your own animation
        
    def timerFired(self):
        

    def redrawAll(self):
        self.canvas.data.person.drawPerson(self.canvas)

    def run(self):
        # create the root and the canvas
        global root
        root = Tk()
        windowWidth = 700
        windowHeight = 500
        self.canvas = Canvas(root, width=windowWidth, height=windowHeight)
        root.resizable(width=FALSE, height=FALSE)
        # change mouse cursor
        root.config(cursor="plus")
        root.title('HackCMU')
        self.canvas.pack()
        # Store canvas in root and in canvas itself for callbacks
        #root.canvas = canvas.canvas = canvas
        # Set up canvas data and call init
        class Struct: pass
        self.canvas.data = Struct()
        self.canvas.data.windowWidth = windowWidth
        self.canvas.data.windowHeight = windowHeight
        self.canvas.data.person = Person(self.canvas)
        self.canvas.data.person.drawPerson(self.canvas)

        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll()
        def mousePressedWrapper(event):
            self.mousePressed(event)
            redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()
        # set up events
        root.bind("<Key>", keyPressedWrapper)
        # set up timerFired events
        self.timerFiredDelay = 250 # milliseconds
        def timerFiredWrapper():
            self.timerFired()
            redrawAllWrapper()
            # pause, then call timerFired again
            self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
        # init and get timerFired running
        timerFiredWrapper()        
        # and launch the app
        root.mainloop()  
        # This call BLOCKS (so your program waits until you close the window!)

game = mainGame()
game.run()
