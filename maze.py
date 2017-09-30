from pgraph.graph import Graph
from queue.queue import Queue

def printmaze(maze):
	for row in maze:
		for col in row:
			print "%2s" % col,
		print('\n')
	print('\n')

""" Takes file name, and return 2d list representation from contents of the file. """
def getMazeFromFile(mazeFile):
	f = open(mazeFile, 'r')
	result = []

	for line in f:
		# Remove all white space characters from end of line.
		row = list(line.rstrip())
		result.append(row)
	f.close()
	return list(map(int, row) for row in result) # Convert str to int for every character in the file.

def getMazeIndexes(maze):
	result = []
	numRows = len(maze)
	numCols = len(maze[0])
	for i in range(numRows):
		row = []
		for j in range(numCols):
			index = posToId(i, j, numCols)
			row.append(index)
		result.append(row)
	return result

""" Takes index of row, col and number of cols,
and return unique id for current position. """
def posToId(row, col, numCols):
	return row*numCols+col

""" In the maze 0 (zero) means that path exist,
and 1 (one) means dead end. """
def buildGraph(mazeFile):

	# Get 2d list representation of the maze.
	charList = getMazeFromFile(mazeFile)
	# Create graph
	mazeGraph = Graph()
	curVertex = None
	rightNbr = None
	bottomNbr = None
	numRows = len(charList)
	numCols = len(charList[0])

	for i in range(numRows):
		for j in range(numCols):
			# Check path exist.
			if charList[i][j] == 0:
				# Get unique id for current position.
				curVertex = posToId(i, j, numCols)

				# The bottom border is still not reached.
				if i < numRows - 1:
					# Check if bottom neighbor value is zero.
					if charList[i+1][j] == 0:
						# Get unique id for bottom neighbor.
						bottomNbr = posToId(i+1, j, numCols)
				# The right border is still not reached.
				if j < numCols - 1:
					# Check if right neighbor value is zero.
					if charList[i][j+1] == 0:
						# Get unique id for right neighbor.
						rightNbr = posToId(i, j+1, numCols)

				if curVertex != None:
					if bottomNbr:
						# Add edge between current vertex and his bottom neighbor,
						# pre-creating them if they don't exist.
						mazeGraph.addEdge(curVertex, bottomNbr)
						bottomNbr = None
					if rightNbr:
						# Add edge between current vertex, and his right neighbor,
						# pre-creating them if they don't exist.
						mazeGraph.addEdge(curVertex, rightNbr)
						rightNbr = None
					curVertex = None

	return mazeGraph

# (breadth-first search)
def bfs(start):
	start.setDistance(0)
	start.setPred(None)
	# Queue for hold vertexes.
	vertQueue = Queue()
	vertQueue.enqueue(start)

	while vertQueue.size() > 0:
		# Get first value from queue.
		curVertex = vertQueue.dequeue()
		# Go through all the neigbors of the current vertex.
		for nbr in curVertex.getConnections():
			# Check if the neighbor was not achieved.
			if nbr.getColor() == 'white':
				# Mark neighbor as achieved.
				nbr.setColor('grey')
				# Compute distance between current vertex and neighbor.
				nbr.setDistance(curVertex.getDistance() + 1)
				# Set predecessor as a current vertex for,
				# for afterwards recreate the path.
				nbr.setPred(curVertex)
				# Add neighbor to end of queue.
				vertQueue.enqueue(nbr)
		# Mark current vertex as passed.
		curVertex.setColor('black')

# (depth-first search)
def dfs(start, end):
	# Check if the vertex was achieved.
	if start.getColor() != 'white':
		return

	# Mark vertex as passed.
	start.setColor('black')
	# Check if we don't reached exit.
	if start == end:
		print('The path was found!\n')
		return

	# Go through all the neigbors of the current vertex.
	for nbr in start.getConnections():
		# Set predecessor as a current vertex for,
		# for afterwards recreate the path.
		nbr.setPred(start)
		# Call dfs for neighbor.
		dfs(nbr, end)

def traverse(y):
	if y is None: return "The path don't exist."
	x = y
	thepath = []
	while x.getPred():
		thepath.insert(0, x.getId())
		x = x.getPred()
	thepath.insert(0, x.getId())
	return thepath


if __name__ == '__main__':
	# Get maze from file and return as the list
	maze = getMazeFromFile('./maze.txt')
	# Get index of every element in maze and return as hte list
	mazeIndexes = getMazeIndexes(maze)
	printmaze(maze)
	printmaze(mazeIndexes)

	# Bulid graph from file
	G = buildGraph('./maze.txt')
	# bfs(G.getVertex(0))
	# Pass entry and exit vertexes, for looking for the path.
	dfs(G.getVertex(0), G.getVertex(24))
	# Print the path if exist.
	print(traverse(G.getVertex(24)))
