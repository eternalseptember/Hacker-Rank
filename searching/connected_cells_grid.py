"""
Consider a matrix with n rows and m columns, where each cell contains
either a 0 or a 1 and any cell containing a 1 is called a filled cell.
Two cells are said to be connected if they are adjacent to each other
horizontally, vertically, or diagonally.

If one or more filled cells are also connected, they form a region.
Note that each cell in a region is connected to at least one other cell
in the region but is not necessarily directly connected to all the other
cells in the region.

Task:
Given an n x m matrix, find and print the number of cells in the largest
region in the matrix. Note that there may be more than one region in the
matrix.

Input Format:
The first line contains an integer, n, denoting the number of rows in the
matrix. 
The second line contains an integer, m, denoting the number of columns in
the matrix. 
Each line i of the n subsequent lines contains m space-separated integers
describing the respective values filling each row in the matrix.
"""


def find_largest_region(n, m, matrix):
	filled_cells = []
	connected_cells = []
	unconnected_cells = []
	largest_region = 0

	# 1.) Get the list of filled cells' coordinates.
	for row in range(n):
		for col in range(m):
			if matrix[row][col] == 1:
				filled_cells.append((row, col))

	# 2.) Match them up into regions.
	passes = 0
	while len(filled_cells) > 0:
		cell = filled_cells.pop(0)

		# the first cell sets the region
		if len(connected_cells) == 0:
			connected_cells.append(cell)
		else:
			if is_connected_to_list(connected_cells, cell):
				connected_cells.insert(0, cell)
			else:
				unconnected_cells.append(cell)

		# after the filled_cells list empties and before the 'while' loop iterates again...
		if (len(filled_cells) == 0):
			filled_cells = unconnected_cells[:]
			unconnected_cells.clear()

			# after the filled_cells list is empty the first time,
			# check the remaining unconnected cells again
			if (passes == 0) and (len(filled_cells) > 0):
				passes = 1
			else:
				# find the size of a region
				size = len(connected_cells)
				if size > largest_region:
					largest_region = size
				
				connected_cells.clear()
				passes = 0

	return largest_region


def is_connected_to_list(list_of_cells, cell):
	found = False

	for connected_cell in list_of_cells:
		connected = is_connected(connected_cell, cell)

		if connected:
			found = True
			break

	return found


def is_connected(unknown_cell, cell):
	(c_x, c_y) = unknown_cell
	(x, y) = cell

	if (c_x == (x - 1)):
		if (c_y == (y - 1)) or (c_y == y) or (c_y == (y + 1)):
			return True
		else:
			return False
	elif (c_x == x):
		if (c_y == (y - 1)) or (c_y == (y + 1)):
			return True
		else:
			return False
	elif (c_x == (x + 1)):
		if (c_y == (y - 1)) or (c_y == y) or (c_y == (y + 1)):
			return True
		else:
			return False
	else:
		return False


"""
n = int(input().strip())
m = int(input().strip())

matrix = []
for i in range(n):
	line = [int(temp) for temp in input().strip().split(' ')]
	matrix.append(line)

largest_area = find_largest_region(n, m, matrix)
print(largest_area)
"""


# setting up test case 1
# expected answer: 5
n = 4  # rows
m = 4  # columns
in_str1 = ['1 1 0 0', '0 1 1 0', '0 0 1 0', '1 0 0 0']

matrix = []
for i in range(n):
	line = [int(temp) for temp in in_str1[i].strip().split(' ')]
	matrix.append(line)

largest_area = find_largest_region(n, m, matrix)
print(largest_area)


# setting up test case 2
# expected answer: 9
n = 7  # rows
m = 5  # columns
in_str1 = ['1 1 1 0 1', '0 0 1 0 0', '1 1 0 1 0', '0 1 1 0 0', '0 0 0 0 0', '0 1 0 0 0', '0 0 1 1 0']

matrix = []
for i in range(n):
	line = [int(temp) for temp in in_str1[i].strip().split(' ')]
	matrix.append(line)

largest_area = find_largest_region(n, m, matrix)
print(largest_area)


# setting up test case 3
# expected answer: 8
n = 5  # rows
m = 4  # columns
in_str1 = ['0 0 1 1', '0 0 1 0', '0 1 1 0', '0 1 0 0', '1 1 0 0']

matrix = []
for i in range(n):
	line = [int(temp) for temp in in_str1[i].strip().split(' ')]
	matrix.append(line)

largest_area = find_largest_region(n, m, matrix)
print(largest_area)

