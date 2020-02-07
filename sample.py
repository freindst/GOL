import random

class board:
  Width = 50
  Height = 50
  count = 0

  def __init__(self):
    self.cells = []
    for y in range(0, self.Height):
      row = []
      for x in range(0, self.Width):
        row.append(cell())
      self.cells.append(row)

  def getCell(self, x, y):
    y_fix = y % self.Height
    x_fix = x % self.Width
    return self.cells[y_fix][x_fix]

  def setCell(self, x, y, alive):
    cell = self.getCell(x, y)
    cell.isAlive = alive

  def randomGenerateBoard(self):
    live_rate = 0.2
    for y in range(0, self.Height):
      for x in range(0, self.Width):
        r = random.random()
        self.setCell(x, y, r <= live_rate)

  def display(self):
    for y in range(0, self.Height):
      line = ''
      for x in range(0, self.Width):
        current_cell = self.getCell(x, y)
        line = line + current_cell.toString()
      print(line)

  def nextGeneration(self):
    newBoard = board()
    for y in range(0, self.Height):
      for x in range(0, self.Width):
        newBoard.setCell(x, y, self.isCellAlive(x, y))
    newBoard.count = self.count + 1
    return newBoard

  def getNeighbors(self, x, y):
    neighbors = []
    neighbors.append(self.getCell(x - 1, y - 1))
    neighbors.append(self.getCell(x, y - 1))
    neighbors.append(self.getCell(x + 1, y - 1))
    neighbors.append(self.getCell(x - 1, y))
    neighbors.append(self.getCell(x + 1, y))
    neighbors.append(self.getCell(x - 1, y + 1))
    neighbors.append(self.getCell(x, y + 1))
    neighbors.append(self.getCell(x + 1, y + 1))
    return neighbors
  
  def isCellAlive(self, x, y):
    neighbors = self.getNeighbors(x, y)
    num = 0
    for n in neighbors:
      if n.isAlive:
        num = num + 1
    currentCell = self.getCell(x, y)
    if currentCell.isAlive:
      return num == 2 or num == 3
    else:
      return num == 3


class cell:
  death = '_'
  live = 'X'

  def __init__(self):
    self.isAlive = False

  def toString(self):
    if self.isAlive:
      return self.live
    else:
      return self.death

a = board()
a.randomGenerateBoard()
a.display()

def promp():
  global a
  i = input("Press 'Blade' to continue: ")
  if i == 'c':
    a = a.nextGeneration()
    a.display()
    print("New generation " + str(a.count))
    print()
    promp()

promp()