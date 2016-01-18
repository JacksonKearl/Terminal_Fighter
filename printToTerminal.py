# This utility renders the given characters to the terminal, assuming what is passed to it is the correct amount of
# characters for the given terminal size.
import sys

class printRender():
	def __init__(self, dataToRender, terminalSize):
		self.printToTerminal(dataToRender, terminalSize)

	def printToTerminal(self, pointDict, terminalSize):
		terminalWidth = terminalSize[0]
		terminalHeight = terminalSize[1]
		for y in range(terminalHeight):
			for x in range(terminalWidth):
				sys.stdout.write(pointDict[y][x])
		print('') # For some reason end='' and stdout don't print until the function is done running, hence this
