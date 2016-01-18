# This utility creates a renderable string list by the renderToTerminal module.

class CreateRenderable():
	def __init__(self, pointsToDraw, terminalSize):
		width = terminalSize[0]
		height = terminalSize[1]
		empty = self.createEmptyDictMatrix(height, width)
		self.renderable = self.getRender(pointsToDraw, width, height, empty)

	def getRender(self, pointDict, width, height, empty):
		for point in pointDict:
			x, y = point[0], point[1]
			empty[y][x] = pointDict[point]
		return empty

	def createEmptyDictMatrix(self, terminalHeight, terminalWidth):
		empty = {}
		for y in range(terminalHeight):
			empty[y] = {}
			for x in range(terminalWidth):
				empty[y][x] = " "
		return empty
