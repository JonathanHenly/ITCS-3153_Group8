# GridIO.py
#
# Author:  Jonathan Henly
#   Date:  1-26-2019
#  Class:  ITCS 3153-001

class GridIO:

	# read a grid from a specified file
	@staticmethod
	def ReadGrid(filename):
		grid = []
		with open(filename, 'r') as f:
			for line in f.readlines():
				grid.append(list(map(int, line.strip().split(' '))))
		return grid

	# write a passed in grid to a specified file
	@staticmethod
	def WriteGrid(filename, grid):
		with open(filename, 'w') as altf:
			for row in grid:
				for col in row:
					altf.write(str(col) + ' ')
				altf.write('\n')

# modify a specified location in the grid
def ModifyGrid(grid, location, value):
	grid[location[0]][location[1]] = value

# find all zeros in grid
def FindAllFreeLocs(grid):
	free = []
	r = 0
	for row in grid:
		for col in range(len(row)):
			if grid[r][col] == 0:
				free.append([r, col])
		r += 1
	return free


import random

# main function definition
def main():
	g = GridIO.ReadGrid("./grid.txt")
	print(g)
	free = FindAllFreeLocs(g)
	for loc in free:
		ModifyGrid(g, [loc[0], loc[1]], int((9-2)*random.random() + 2))
	print(g)
	GridIO.WriteGrid('./out_grid.txt', g)


# main function call
main()

