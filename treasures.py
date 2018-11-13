import random

class Treasure:

	def __init__(self, type, pos):
		self.type = type
		self.pos = pos
	
	def getType(self):
		return self.type

	def getPos(self):
		return self.pos

class TreasureManager:
	class __TreasureManager:
		typeList = [
			{
				"name": "sword",
				"life": 0,
				"attack": 1,
				"accuracy": 0.8,
				"shield": 0
			},
			{
				"name": "armor",
				"life": 0,
				"attack": 0,
				"accuracy": 0,
				"shield": 1
			},
			{
				"name": "health",
				"life": 20,
				"attack": 0,
				"accuracy": 0,
				"shield": 0
			}
		]

		def __init__(self):
			self.treasures = []

		def addTreasure(self, pos):
			random.seed()
			type  = self.typeList[random.randrange(0, len(self.typeList))]
			self.treasures.append(Treasure(type, pos))

		def getTreasureByPos(self, pos):
			for treasure in self.treasures:
				treasurePos = treasure.getPos()
				if pos == treasurePos:
					self.treasures.remove(treasure)
					return treasure.getType()
			return None
	
	instance = None

	def __init__(self):
		if not TreasureManager.instance:
			TreasureManager.instance = TreasureManager.__TreasureManager()

	def addTreasure(self, pos):
		TreasureManager.instance.addTreasure(pos)
	
	def getTreasureByPos(self, pos):
		return TreasureManager.instance.getTreasureByPos(pos)
