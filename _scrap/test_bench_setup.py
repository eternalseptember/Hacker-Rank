from __ import *

# Set up for executing test cases.
test_cases = [0, 3, 5, 6]

# Personal test cases start in the 100s
# test_cases = [1000]

for num in test_cases:
	# Setting up the directory and file names.
	# Expects the files to be named like '0-in.txt' and '0-out.txt'
	dir_name = 'test_cases/'
	problem_name = '__/'  # FILL IN PROBLEM NAME HERE
	ext = '.txt'
	str_results = dir_name + problem_name + str(num) + '-results' + ext
	str_inputs = dir_name + problem_name + str(num) + '-in' + ext
	str_expected = dir_name + problem_name + str(num) + '-out' + ext

	# Open file streams.
	test_case_results = open(str_results, 'w')
	test_case_inputs = open(str_inputs, 'r')
	test_case_expected = open(str_expected, 'r')

	"""
	# For testing that files opened successfully.
	if test_case_results:
		print('test_case_results opened!')
	if test_case_inputs:
		print('test_case_inputs opened!')
	if test_case_expected:
		print('test_case_expected opened!')
	"""

	# That constant first line in HR's setup.
	inp = test_case_inputs.readline().strip()
	T = int(inp)

	# Before looping with T:

	# Do something T times.
	for i in range(T):
		inp = test_case_inputs.readline().strip()
		N, M = (int(temp) for temp in inp.split(' '))

		"""
		# Example on how to set up matrix input.
		matrix = []
		for j in range(N):
			inp = test_case_inputs.readline().strip()
			row = list(inp)
			matrix.append(row)
		"""

		# Get the actual result.
		# Results of most problems from HR is returned from a function.
		count = function_Name(N, M, matrix)

		# Modified this a bit to pass in a file stream for writing.
		# count = function_name(N, M, matrix, test_case_results)
		act = count

		# Get the expected result.
		exp = test_case_expected.readline().strip()

		# Do some type conversion first:
		if type(act) == int:
			exp = int(exp)

		# Write the results to file.
		test_case_results.write('EXP: {0}  ACT: {1}\n'.format(exp, act))

		"""
		# Write the failed results to file.
		if exp != act:

			# example on how to print a matrix to file
			matr_str = ''
			for row in matrix:
				matr_str += ''.join(str(x) for x in row)
				matr_str += '\n'
			test_case_results.write(matr_str)
		"""

	# After looping with T:
	# Might need to copy and paste file write functions here.

	# Close the file streams.
	test_case_results.close()
	test_case_inputs.close()
	test_case_expected.close()


print('Done!')
