# pgraph/vertex.py

""" Class for representation vertex object in the graph """
class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = dict()
		self.color = 'white'
		self.distance = 0
		self.pred = None

	def setDistance(self, distance):
		self.distance = distance

	def setPred(self, pred):
		self.pred = pred

	def getPred(self):
		return self.pred

	def getDistance(self):
		return self.distance

	def getColor(self):
		return self.color

	def setColor(self, color):
		self.color = color

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + ' connectedTo: ' + \
			   str([x.id for x in self.connectedTo])

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]
