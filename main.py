# HackCMU 2013
# Weiqi Cai, Megan Chen, Lina Li, Teng Zhang

from Tkinter import *

class Platform(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.row = 20
        self.col = 30
        self.width = canvas.data.windowWidth/self.col

    def drawPlatform(self,canvas):
        matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        for i in xrange(self.row):
            for j in xrange(self.col):
                if matrix[i][j] == 1:
                    canvas.create_rectangle(self.width*j, self.width*i,
                        self.width*(j+1),self.width*(i+1),fill="black")

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

    def update(self, canvas):
        self.canvas.data.person.centerX += self.speedX
        self.canvas.data.person.centerY += self.speedY
        self.speedY+=5

    def run(self):
        if self.heading:
            self.centerX += self.speedX
        else: self.centerX -= self.speedX

    def jump(self):
        self.centerY += self.speedY
        


###########################################
# Game class
###########################################

class mainGame(object):
    def keyPressed(self, event):
        if (event.keysym == "a" or event.keysym == "Left"):
            self.canvas.data.person.heading = False
            #self.canvas.data.person.run()
            #redrawAll()# use this state for char dir. facing
        if (event.keysym == "d" or event.keysym == "Right"):
            self.canvas.data.person.heading = True
            #self.canvas.data.person.run()   
        if (event.keysym == "w" or event.keysym == "Up"):
            self.canvas.data.person.jumping = True
            self.canvas.data.person.speedY = -20
        if (event.keysym == "p"):
            self.isPaused = not self.isPaused
    # Override these methods when creating your own animation
        
    def timerFired(self):
        self.canvas.data.person.update(self.canvas)
        #self.canvas.data.person.right += 1
        #self.canvas.data.person.moveLeft(self.canvas)

    def redrawAll(self):
        self.canvas.data.person.drawPerson(self.canvas)
        self.canvas.data.platform.drawPlatform(self.canvas)

    def run(self):
        # create the root and the canvas
        global root
        root = Tk()
        windowWidth = 600
        windowHeight = 400
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
        self.canvas.data.platform = Platform(self.canvas)
        self.canvas.data.platform.drawPlatform(self.canvas)
        
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
        self.timerFiredDelay = 100 # milliseconds
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
