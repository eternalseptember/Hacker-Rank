"""
Note: You can move the castle from cell (a,b) to any (x,y) in a
single step if there is a straight line between (a,b) and (x,y) that
does not contain any forbidden cell. Here, "X" denotes a forbidden
cell.

Input Format:
The first line contains an integer N, the size of the grid.

The following N lines contains a string of length N that consists
of one of the following characters: "X" or ".". Here, "X" denotes
a forbidden cell, and "." denotes an allowed cell.

The last line contains a, b, denoting the initial position of the
castle, and c, d, denoting the goal position. Here, a, b, c, and d
are space separated.

Output Format:
Output a single line: The integer denoting the minimum number of steps
required to move the castle to the goal position.
"""


def find_steps(N, grid, a, b, c, d):
	# setting up the solutions map
	path = [[0 for col in range(N)] for row in range(N)]
	path[a][b] = 1
	path[c][d] = '*'

	find_path(N, grid, a, b, path)

	return 0


def find_path(size, maze, a, b, path):
	queue = []
	queue.append((a, b))
	found = False

	while found is False:
		point = queue.pop()
		row, col = (point)
		step = path[row][col]

		# north, east, south, west
		four_dirs = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]

		for direction in four_dirs:
			new_row, new_col = (direction)

			if not in_bound(size, maze, direction):
				continue
			if maze[new_row][new_col] == 'X':
				path[new_row][new_col] = -1

			if path[new_row][new_col] == 0:
				path[new_row][new_col] = step + 1
				queue.append((new_row, new_col))
			elif path[new_row][new_col] == '*':
				found = True

	for line in path:
		print(line)


def in_bound(size, maze, point):
	row, col = (point)
	if (row < 0) or (row >= size):
		return False
	if (col < 0) or (col >= size):
		return False
	return True



"""
N = int(input().strip())

grid = []
for i in range(N):
	row = list(input().strip())
	grid.append(row)

a, b, c, d = (int(temp) for temp in input().strip().split(' '))

steps = find_steps(N, grid, a, b, c, d)
print(steps)
"""


# Setting up test case 1
# Expected answer: 3
N = 3  # size of the grid
in_str1 = ['.X.', '.X.', '...']
in_str2 = '0 0 0 2'

grid = []
for i in range(N):
	row = list(in_str1[i].strip())
	grid.append(row)

a, b, c, d = (int(temp) for temp in in_str2.strip().split(' '))

steps = find_steps(N, grid, a, b, c, d)
print(steps)


