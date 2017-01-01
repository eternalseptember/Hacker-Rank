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
	count = 0
	portkey_pos = None
	start_pos = None

	# find the porkey and starting positions
	for i in range(N):  # rows
		for j in range(M):  # cols
			if matrix[i][j] == '*':
				portkey_pos = (i, j)
			if matrix[i][j] == 'M':
				start_pos = (i, j)

			if (portkey_pos is not None) and (start_pos is not None):
				break

		if (portkey_pos is not None) and (start_pos is not None):
				break

	print('Portkey: {0}'.format(portkey_pos))
	print('Starting: {0}'.format(start_pos))

	return count


# def have_mult_paths(x, y):
	# possible choices: left, right, up, down
	# take out backwards direction


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


T = 3
in_str1 = ['2 3', '4 11', '4 11']
in_str2 = [['*.M', '.X.'],
		   ['.X.X......X', '.X*.X.XXX.X', '.XX.X.XM...', '......XXXX.'],
		   ['.X.X......X', '.X*.X.XXX.X', '.XX.X.XM...', '......XXXX.']]
in_str3 = ['1', '3', '4']


for i in range(T):
	N, M = (int(temp) for temp in in_str1[i].strip().split(' '))

	matrix = []
	for j in range(N):
		row = list(in_str2[i][j].strip())
		matrix.append(row)

	K = int(in_str3[i].strip())

	if count_multiple_paths(N, M, matrix) == K:
		print('Impressed')
	else:
		print('Oops!')





