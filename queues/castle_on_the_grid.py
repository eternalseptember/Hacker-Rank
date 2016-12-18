"""
Note: You can move the castle from cell (a,b) to any (x,y) in a
single step if there is a straight line between  and (a,b) that
does not contain any forbidden cell. Here, "X" denotes a forbidden
cell.

Input Format:
The first line contains an integer N, the size of the grid.

The following N lines contains a string of length N that consists
of one of the following characters: "X" or ".". Here, "X" denotes
a forbidden cell, and "." denotes an allowed cell.

The last line contains a, b, denoting the initial position of the
castle, and c, c, denoting the goal position. Here, a, b, c, and d
are space separated.

Output Format:
Output a single line: The integer denoting the minimum number of steps
required to move the castle to the goal position.
"""


def find_steps(N, grid, start_pos, end_pos):
	(a, b) = (start_pos)
	(c, d) = (end_pos)
	return 0



"""
N = int(input().strip())

grid = []
for i in range(N):
	row = list(input().strip())
	grid.append(row)

a, b, c, d = input().strip().split(' ')

steps = find_steps(N, grid, (a, b), (c, d))
print(steps)
"""


N = 3  # size of the grid
in_str1 = ['.X.', '.X.', '...']
in_str2 = '0 0 0 2'

grid = []
for i in range(N):
	row = list(in_str1[i].strip())
	grid.append(row)

a, b, c, d = in_str2.strip().split(' ')

steps = find_steps(N, grid, (a, b), (c, d))
print(steps)


