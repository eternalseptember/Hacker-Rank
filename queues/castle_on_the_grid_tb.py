from castle_on_the_grid import *

# Set up for executing test cases.
test_cases = [3]


for num in test_cases:
	# setting up the directory and file names
	# expects the files to be named like '0-in.txt' and '0-out.txt'
	dir_name = 'test_cases/'
	problem_name = 'castle_on_the_grid/'  # FILL IN PROBLEM NAME HERE
	ext = '.txt'
	str_results = dir_name + problem_name + str(num) + '-results' + ext
	str_inputs = dir_name + problem_name + str(num) + '-in' + ext
	str_expected = dir_name + problem_name + str(num) + '-out' + ext

	# open file streams
	test_case_results = open(str_results, 'w')
	test_case_inputs = open(str_inputs, 'r')
	test_case_expected = open(str_expected, 'r')

	"""
	# for testing file opened successfully
	if test_case_results:
		print('test_case_results opened!')
	if test_case_inputs:
		print('test_case_inputs opened!')
	if test_case_expected:
		print('test_case_expected opened!')
	"""

	# that constant first line in HR's setup
	inp = test_case_inputs.readline().strip()
	N = int(inp)

	# do something with N
	grid = []
	# varies per problem
	for i in range(N):
		inp = test_case_inputs.readline().strip()
		row = list(inp)
		grid.append(row)

	inp = test_case_inputs.readline().strip()
	a, b, c, d = (int(temp) for temp in inp.split(' '))

	# get the actual result
	# results of most problems from HR is returned from a function
	steps = find_steps(N, grid, a, b, c, d)
	act = steps

	# modified this a bit to pass in a file stream for writing
	# steps = find_steps(N, grid, a, b, c, d, test_case_results)

	# get the expected result
	exp = test_case_expected.readline().strip()

	# write the result to file
	test_case_results.write('EXP: {0}  ACT: {1}\n'.format(exp, act))

	"""
	# write the failed results to file
	if exp != act:

		# example on how to print a matrix to file
		matr_str = ''
		for row in matrix:
			matr_str += ''.join(str(x) for x in row)
			matr_str += '\n'
		test_case_results.write(matr_str)
	"""

	# close the file streams
	test_case_results.close()
	test_case_inputs.close()
	test_case_expected.close()


print('Done!')
