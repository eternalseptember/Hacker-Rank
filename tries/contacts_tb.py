from contacts import *

# Set up for executing test cases.
test_cases = [1, 12, 100]

# Personal test cases start in the 100s
# test_cases = [1000]

for num in test_cases:
	# Setting up the directory and file names.
	# Expects the files to be named like '0-in.txt' and '0-out.txt'
	dir_name = 'test_cases/'
	problem_name = 'contacts/'  # FILL IN PROBLEM NAME HERE
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
	head = Trie_Node()

	# Do something T times.
	for i in range(T):
		inp = test_case_inputs.readline().strip()
		opp, name = inp.strip().split()

		# Get the actual result.
		if opp == 'add':
			head = insert(head, name)
		else:
			act = find_partial(head, name)
			test_case_results.write('{0}\n'.format(act))


		"""
		# Write the failed results to file.
		if exp != act:


		"""



	# After looping with T:


	# Close the file streams.
	test_case_results.close()
	test_case_inputs.close()
	test_case_expected.close()


print('Done!')
