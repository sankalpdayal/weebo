import Utility as utils
class World:
	staticObjects = []
	movingObjects = []
	room = []
	def __init__(self):
		self.staticObjects = []
		self.movingObjects = []
		self.room = []
		print('World created')

	def addRoom(self,roomAdd):
		self.room = roomAdd
		print('Room added')
		#roomDesign = utils.readLayout(roomAdd + '/Layout.png')
		#roomParams = utils.readParams(roomAdd + '/Layout.txt')