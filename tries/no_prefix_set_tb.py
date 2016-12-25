from no_prefix_set import *

# Set up for executing test cases.
test_cases = [37, 38, 39]

# Personal test cases start in the 100s
# test_cases = [1000]

for num in test_cases:
	# Setting up the directory and file names.
	# Expects the files to be named like '0-in.txt' and '0-out.txt'
	dir_name = 'test_cases/'
	problem_name = 'no_prefix_set/'  # FILL IN PROBLEM NAME HERE
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
	strings = []

	# Do something T times.
	for i in range(T):
		inp = test_case_inputs.readline().strip()
		strings.append(inp)


	# After looping with T:
	# Get the actual result.
	# Results of most problems from HR is returned from a function.
	failed_string = check_prefixes(strings)

	# problem-specific modification
	if failed_string is None:
		result = 'GOOD SET'
	else:
		result = 'BAD SET'

	# problem-specific results modification
	act1 = failed_string
	act2 = result

	# Get the expected result.
	exp1 = test_case_expected.readline().strip()
	exp2 = test_case_expected.readline().strip()


	# Write the results to file.
	test_case_results.write('EXP: {0}  ACT: {1}\n'.format(exp1, act1))
	test_case_results.write('EXP: {0}  ACT: {1}\n'.format(exp2, act2))

	"""
	# Write the failed results to file.
	if exp != act:


	"""

	# Close the file streams.
	test_case_results.close()
	test_case_inputs.close()
	test_case_expected.close()


print('Done!')
