class Obstacle(Object):
	def __init__(self, canvas):
		#maybe generate a random width and height based on certain
		#range of numbers
		self.width = 100
		self.height = 20
		self.canvas = canvas
		self.centerX = 100
		self.centerY = 100
		self.isTouched = False
