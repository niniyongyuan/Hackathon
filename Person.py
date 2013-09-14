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
		self.speed = 5
		self.jumping = False
		self.faceLeft = False

	def drawPerson(self, canvas):
		left = self.centerX - self.radius
		right = self.centerX + self.radius
		top = self.centerY - self.radius
		bottom = self.centerY + self.radius
		#change it to load the person
		canvas.create_oval(left, right, top, bottom, fill="red")

	def run(self, canvas):
		self.centerX += self.speed


	def jump(self, canvas):
		self.centerY += self.speed
