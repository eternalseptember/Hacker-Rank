from shortest_reach import *

# Set up for executing test cases.
test_cases = [5, 6]

# Personal test cases start in the 100s
# test_cases = [1000]

for num in test_cases:
	# Setting up the directory and file names.
	# Expects the files to be named like '0-in.txt' and '0-out.txt'
	dir_name = 'test_cases/'
	problem_name = 'shortest_reach/'  # FILL IN PROBLEM NAME HERE
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
		n, m = (int(temp) for temp in inp.split(' '))

		# problem-specific: get edges list
		edges_list = []
		for j in range(m):
			inp = test_case_inputs.readline().strip()
			u, v = (int(temp) for temp in inp.strip().split(' '))
			edges_list.append((u, v))

		# problem-specific: starting node
		inp = test_case_inputs.readline().strip()
		s = int(inp.strip())



		# Get the actual result.
		# Results of most problems from HR is returned from a function.
		dist_list = calc_distance(n, s, edges_list)

		# Get the expected result.
		exp = test_case_expected.readline().strip()

		# problem-specific: format the answer
		act = ''
		for result in dist_list:
			act += str(result)
			act += ' '
		act += '\n'

		# Write the results to file.
		# test_case_results.write('EXP: {0}  ACT: {1}\n'.format(exp, act))

		# Write the failed results to file.
		if exp != act:
			test_case_results.write(act)


		# Lets me know a test case within HR's input is finished.
		# print('\t\tHR\'s test case completed.')

	# After looping with T:
	# Might need to copy and paste file write functions here.

	# Close the file streams.
	test_case_results.close()
	test_case_inputs.close()
	test_case_expected.close()

	# Lets me know which test case is finished.
	# print('\t\tTest case {0} completed.'.format(num))

print('Done!')
