import world

class Player:
	def __init__(self):
		self.x = 1
		self.y = 2
		
	def move(self, dx, dy):
		self.x += dx
		self.y += dy
	def move_north(self):
		self.move(dx=0, dy=-1)
	def move_south(self):
		self.move(dx=0, dy=1)
	def move_east(self):
		self.move(dx=1, dy=0)
	def move_west(self):
		self.move(dx=-1, dy=0)
		
	def enter_city(self):
		city = 1
		self.x = 0
		self.y = 1
		return city
