"""
M is starting point. * is portkey.

Input Format:
The first line contains an integer, T, the number of test cases.
Each test case is described as follows:
- The first line contains 2 space-separated integers, N and M,
respectively, denoting the forest matrix.
- The N subsequent lines each contain a string of length M describing
a row of the forest matrix.
- The last line contains an integer, K, denoting Ron's guess as to how
many times Hermione will wave her wand.

Output Format:
On a new line for each test case, print 'Impressed' if Ron impresses
Hermione by guessing correctly; otherwise, print 'Oops!'.
"""


def count_multiple_paths(N, M, matrix):
	start_pos = None
	path = [[0 for col in range(M)] for row in range(N)]

	# find the starting position
	for row in range(N):
		for col in range(M):
			if matrix[row][col] == 'M':
				start_pos = (row, col)
				path[row][col] = 1

			if start_pos is not None:
				break

		if start_pos is not None:
			break

	# look for the portkey
	row, col = (start_pos)
	found = find_path(N, M, matrix, row, col, path)

	# count the number of times multiple paths are possible
	if found:
		count = multiple_choices_possible(start_pos, matrix, path, N, M)
	else:
		count = 0

	# print('Count: {0}'. format(count))
	return count


def multiple_choices_possible(start_pos, matrix, path_matrix, N, M):
	count = 0
	row, col = (start_pos)
	found = False

	while found is False:
		# unmark current spot to prevent recursion errors
		path_matrix[row][col] = 0

		possible_directions = 0
		impossible_directions = 0
		adj_to_start = False
		four_directions = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]

		for direction in four_directions:
			new_row, new_col = (direction)
			if not in_bound(N, M, matrix, new_row, new_col):
				impossible_directions += 1
				continue
			if (matrix[new_row][new_col] == '.') or (matrix[new_row][new_col] == '*'):
				possible_directions += 1
			elif (matrix[new_row][new_col] == 'M'):
				adj_to_start = True
			if path_matrix[new_row][new_col] == 1:
				next_pos = (new_row, new_col)

				if matrix[new_row][new_col] == '*':
					found = True

		if (possible_directions >= 3):
			# print('3+ dirs')
			count += 1
		elif (possible_directions == 2):
			if ((row, col) == start_pos):
				# print('fork in starting position')
				count += 1
			elif adj_to_start and (impossible_directions == 1):
				# print('next to edge and start pos')
				count += 1

		row, col = (next_pos)

	return count


def find_path(N, M, matrix, row, col, path_matrix):
	# if the position contains a portkey:
	if matrix[row][col] == '*':
		path_matrix[row][col] = 1
		return True
	# if the position contains a tree:
	if matrix[row][col] == 'X':
		path_matrix[row][col] = -1
		return False

	# mark spot as part of the solution path:
	path_matrix[row][col] = 1

	# search in four directions
	four_directions = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
	for direction in four_directions:
		new_row, new_col = (direction)

		if not in_bound(N, M, matrix, new_row, new_col):
			continue
		# skip if this spot has been visited before
		elif path_matrix[new_row][new_col] != 0:
			continue
		else:
			if find_path(N, M, matrix, new_row, new_col, path_matrix):
				path_matrix[new_row][new_col] = 1
				return True

	# by this point, this spot is not a part of the solution
	path_matrix[row][col] = -1
	return False


def in_bound(N, M, matrix, row, col):
	# valid values for row is range(0, N):
	if (row < 0) or (row >= N):
		return False
	# valid values for col is range(0, M):
	if (col < 0) or (col >= M):
		return False
	return True





"""
T = int(input().strip())
for i in range(T):
	N, M = (int(temp) for temp in input().strip().split(' '))

	matrix = []
	for j in range(N):
		row = list(input().strip())
		matrix.append(row)

	K = int(input().strip())

	if count_multiple_paths(N, M, matrix) == K:
		print('Impressed')
	else:
		print('Oops!')
"""

# First set of test cases:
# Should be Impressed, Impressed, Oops!
T = 2
in_str1 = ['2 3', '4 11']
in_str2 = [['*.M', '.X.'],
		   ['.X.X......X', '.X*.X.XXX.X', '.XX.X.XM...', '......XXXX.']]
in_str3 = ['1', '3']

for i in range(T):
	N, M = (int(temp) for temp in in_str1[i].strip().split(' '))

	matrix = []
	for j in range(N):
		row = list(in_str2[i][j].strip())
		matrix.append(row)

	K = int(in_str3[i].strip())

	# print('Guess: {0}'.format(K))
	if count_multiple_paths(N, M, matrix) == K:
		print('Impressed')
	else:
		print('Oops!')
	# print()

# Second set of test cases
# All should return 'Impressed'.
T = 5
in_str1 = ['3 6', '3 6', '3 6', '3 6', '3 6']
in_str2 = [['*.M...', '.X.X.X', 'XXX...'],
		   ['*..M..', '.X.X.X', 'XXX...'],
		   ['*M....', '.X.X.X', 'XXX...'],
		   ['*....M', '.X.X.X', 'XXX...'],
		   ['*.....', '.X.X.X', 'XXX.M.']]
in_str3 = ['1', '2', '1', '2', '3']

for i in range(T):
	N, M = (int(temp) for temp in in_str1[i].strip().split(' '))

	matrix = []
	for j in range(N):
		row = list(in_str2[i][j].strip())
		matrix.append(row)

	K = int(in_str3[i].strip())

	# print('Guess: {0}'.format(K))
	if count_multiple_paths(N, M, matrix) == K:
		print('Impressed')
	else:
		print('Oops!')
	# print()





