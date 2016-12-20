"""
This is the cleaned up version of the castle_on_the_grid problem.
This version passed all test cases.
Extraneous functions written from my first attempt were removed.
Artifacts from connected test cases were also removed.

Lesson learned: Use pop(0) for QUEUE problems.
"""


def find_steps(N, grid, a, b, c, d):
	# setting up the solutions map
	path = [[0 for col in range(N)] for row in range(N)]
	path[a][b] = 1
	path[c][d] = '*'

	steps_to_goal = find_a_path(N, grid, path, a, b)

	return steps_to_goal


def find_a_path(size, maze, path, a, b):
	queue = []
	queue.append((a, b))
	found = False

	while found is False:
		point = queue.pop(0)
		row, col = (point)
		if point == (a, b):
			step = 1
		else:
			step = path[row][col] + 1

		# north, east, south, west
		four_dirs = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]

		# then fill them
		for dir_num in range(len(four_dirs)):
			direction = four_dirs[dir_num]
			new_row, new_col = (direction)

			if not in_bound(size, maze, direction):
				continue
			if maze[new_row][new_col] == 'X':
				path[new_row][new_col] = -1
				continue

			if path[new_row][new_col] == '*':
				path[new_row][new_col] = step
				found = True

			# if the tile hasn't been visited yet
			elif (path[new_row][new_col] == 0):
				# flood fill
				obstacle = False
				flood_row = new_row
				flood_col = new_col
				while obstacle is False:
					if not in_bound(size, maze, (flood_row, flood_col)):
						obstacle = True
					elif maze[flood_row][flood_col] == 'X':
						path[flood_row][flood_col] = -1
						obstacle = True
					elif path[flood_row][flood_col] == '*':
						path[flood_row][flood_col] = step
						found = True
						obstacle = True
					elif (path[flood_row][flood_col] == 0):
						path[flood_row][flood_col] = step

						if (flood_row, flood_col) not in queue:
							queue.append((flood_row, flood_col))

						# update flood_row or flood_col
						if dir_num == 0:  # north
							flood_row -= 1
						elif dir_num == 1:  # east
							flood_col += 1
						elif dir_num == 2:  # south
							flood_row += 1
						elif dir_num == 3:  # west
							flood_col -= 1
					else:
						# By this point, the content of the cell is smaller than the step
						obstacle = True

			if found is True:
				break

	# for line in path:
	# 	print(line)
	return step


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



