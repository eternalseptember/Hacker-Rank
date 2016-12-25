"""
Given N strings. Each string contains only lowercase letters from a-j
(both inclusive). The set of N strings is said to be GOOD SET if no
string is prefix of another string; else, it is BAD SET. (If two strings
are identical, they are considered prefixes of each other.)

For example, aab, abcde, aabcd is BAD SET because aab is prefix of aabcd.

Print GOOD SET if it satisfies the problem requirement.
Else, print BAD SET and the first string for which the condition fails.

Input Format:
First line contains N, the number of strings in the set.
Then next N lines follow, where i_th line contains i_th string.
"""


def check_prefixes(list_of_strings):
	bad_string = None
	safe_strings = []

	for new_string in list_of_strings:
		if len(safe_strings) == 0:
			# print('First string: {0}'.format(new_string))
			safe_strings.append(new_string)
		else:
			for prefix in safe_strings:
				# print('Checking: {0}  against: {1}'.format(new_string, prefix))
				if new_string.startswith(prefix):
					# print('\tNew string: {0}  starts with: {1}'.format(new_string, prefix))
					return new_string
				if prefix.startswith(new_string):
					# print('\tPrefix: {0}  starts with: {1}'.format(prefix, new_string))
					return new_string

			# by this point, new string is a safe string
			safe_strings.append(new_string)
			# print('\tSafe_strings: {0}'.format(safe_strings))

	# by this point, this is a good set
	return None


"""
N = int(input().strip())
strings = []

for i in range(N):
	str = input().strip()
	strings.append(str)

failed_string = check_prefixes(strings)

if failed_string is None:
	print('GOOD SET')
else:
	print('BAD SET')
	print(failed_string)
"""


# Test case 1 expected result: BAD SET; aabcde
# Test case 2 expected result: BAD SET; aacghgh
N = [7, 4, 4, 4]
in_str1 = [['aab', 'defgab', 'abcde', 'aabcde', 'cedaaa', 'bbbbbbbbbb', 'jabjjjad'],
		   ['aab', 'aac', 'aacghgh', 'aabghgh'],
		   ['aab', 'defgab', 'abc', 'abcde'],
		   ['aab', 'defgab', 'abcde', 'abc']]


for i in range(len(N)):
	strings = []

	for j in range(N[i]):
		str = in_str1[i][j].strip()
		strings.append(str)

	failed_string = check_prefixes(strings)

	if failed_string is None:
		print('GOOD SET')
	else:
		print('BAD SET')
		print(failed_string)
	print()

