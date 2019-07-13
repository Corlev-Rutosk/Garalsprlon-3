class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def intro_text(self):
		raise NotImplementedError("Create a subclass insteaad")
		
class Tile1(MapTile):
	def intro_text(self):
		return """Tile1"""
			
class Tile2(MapTile):
	def intro_text(self):
		return """Tile2"""
		
class Tile3(MapTile):
	def intro_text(self):
		return """Tile3"""
	
class Tile4(MapTile):
	def intro_text(self):
		return """Tile4"""

class Tile5(MapTile):
	def intro_text(self):
		return """Tile 5"""

class Tile6(MapTile):
	def intro_text(self):
		return """Tile6"""
		
class Tile7(MapTile):
	def intro_text(self):
		return """Tile7"""

class Tile8(MapTile):
	def intro_text(self):
		return """Tile 8"""

class Tile9(MapTile):
	def intro_text(self):
		return """Tile 9"""

class Tile10(MapTile):
	def intro_text(self):
		return """Tile10"""

class Tile11(MapTile):
	def intro_text(self):
		return """Tile 11 - city"""


		
		
class Tile12(MapTile):
	def intro_text(self):
		return """Tile 12"""
		
class Tile13(MapTile):
	def intro_text(self):
		return """Tile13"""

class Tile14(MapTile):
	def intro_text(self):
		return """Tile 14"""

class Tile15(MapTile):
	def intro_text(self):
		return """Tile 15"""

class Tile16(MapTile):
	def intro_text(self):
		return """Tile 16"""

		
class Ctile1(MapTile):
	def intro_text(self):
		return """City Tile1"""
			
class Ctile2(MapTile):
	def intro_text(self):
		return """City tile2"""
		
class Ctile3(MapTile):
	def intro_text(self):
		return """City tile3"""
	
class Ctile4(MapTile):
	def intro_text(self):
		return """City tile4"""

class Ctile5(MapTile):
	def intro_text(self):
		return """City tile 5"""

class Ctile6(MapTile):
	def intro_text(self):
		return """City tile6"""
		
class Ctile7(MapTile):
	def intro_text(self):
		return """City tile7"""

class Ctile8(MapTile):
	def intro_text(self):
		return """City tile 8"""

class Ctile9(MapTile):
	def intro_text(self):
		return """Tile 9"""

class Ctile10(MapTile):
	def intro_text(self):
		return """Tile10"""

class Ctile11(MapTile):
	def intro_text(self):
		return """Tile 11"""

class Ctile12(MapTile):
	def intro_text(self):
		return """Tile 12"""
		
class Ctile13(MapTile):
	def intro_text(self):
		return """Tile13"""

class Ctile14(MapTile):
	def intro_text(self):
		return """Tile 14"""

class Ctile15(MapTile):
	def intro_text(self):
		return """Tile 15"""

class Ctile16(MapTile):	
	def intro_text(self):
		return """Tile 16"""



world_map = [
	[Tile1(0,0), Tile2(1,0), Tile3(2,0), Tile4(3,0)],
	[Tile5(0,1), Tile6(1,1), Tile7(2,1), Tile8(3,1)],
	[Tile9(0,2), Tile10(1,2), Tile11(2,2), Tile12(3,2)],
	[Tile13(0,3), Tile14(1,3), Tile15(2,3), Tile16(3,3)]
			]

city_map = [
		[Ctile1(0,0), Ctile2(1,0), Ctile3(2,0), Ctile4(3,0)],
		[Ctile5(0,1), Ctile6(1,1), Ctile7(2,1), Ctile8(3,1)],
		[Ctile9(0,2), Ctile10(1,2), Ctile11(2,2), Ctile12(3,2)],
		[Ctile13(0,3), Ctile14(1,3), Ctile15(2,3), Ctile16(3,3)]
			]
			
def tile_at(x, y):	
	if x<0 or y<0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None
		
def city_tile_at(x, y):	
	if x<0 or y<0:
		return None
	try:
		return city_map[y][x]
	except IndexError:
		return None