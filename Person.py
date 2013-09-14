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
		self.speed = 2
		self.jumping = False
		self.faceLeft = False

	def drawPerson(self, canvas):
		self.left = self.centerX - self.radius
		self.right = self.centerX + self.radius
		self.top = self.centerY - self.radius
		self.bottom = self.centerY + self.radius
		#change it to load the person
		canvas.create_oval(self.left, self.right, self.top, self.bottom, fill="red")

	def run(self):
		self.centerX += self.speed


	def jump(self):
		self.centerY += self.speed
