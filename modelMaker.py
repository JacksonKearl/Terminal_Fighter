# This script allows you to make and export models
# use store instead of deepcopy, revise init function &
# local variables, move print module to update, chnage
# naming.

import makeRender, printToTerminal, terminalSize, getch, math, copy

class Make():
	def __init__(self):
		self.initialTerminalSize = terminalSize.getTerminalSize()
		self.terminalWidth = self.initialTerminalSize[0]
		self.terminalHeight = self.initialTerminalSize[1]
		self.terminalMiddle = (math.floor(self.terminalWidth/2), math.floor(self.terminalHeight/2))
		self.initialCursorPos = self.terminalMiddle
		self.initialRenderObject = makeRender.CreateRenderable({}, self.initialTerminalSize)
		self.initialRenderDict = self.initialRenderObject.renderable
		self.main()

	def main(self):
		renderDict = self.initialRenderDict
		cursorPos = self.initialCursorPos
		x = cursorPos[0]
		y = cursorPos[1]
		cursorRenderDict = self.addCursor(x, y, renderDict)
		self.updatePoints(cursorRenderDict)
		while True:
			x = cursorPos[0]
			y = cursorPos[1]
			key = getch.getch()
			if key == "p":
				return
			if key in "wsad":
				if key == "w":
					y -= 1
				elif key == "s":
					y += 1
				elif key == "a":
					x -= 1
				elif key == "d":
					x += 1
				else:
					pass
				cursorPos = (x, y)
			elif key == "h":
				renderDict[y][x] = "%"
			elif key == "j":
				renderDict[y][x] = " "
			elif key == "f":
				infile = open("./mapping", "w")
				infile.write(str(renderDict))
				infile.close()
			elif key == "l":
				infile = open("./mapping", "r")
				dictString = infile.read()
				renderDict = eval(dictString)
				infile.close()
			elif key == "i":
				print(renderDict)
			else:
				pass
			cursorRenderDict = self.addCursor(x, y, renderDict)
			self.updatePoints(cursorRenderDict)

	def addCursor(self, x, y, renderDict):
		cursorRenderDict = copy.deepcopy(renderDict)
		cursorRenderDict[y][x] = "#"
		return cursorRenderDict

	def updatePoints(self, renderDict):
		size = self.initialTerminalSize
		printToTerminal.printRender(renderDict, size)

Make()
