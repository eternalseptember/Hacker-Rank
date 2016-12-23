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
	# return None for good set
	# return first string for which condition fails
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
N = [7, 4]
in_str1 = [['aab', 'defgab', 'abcde', 'aabcde', 'cedaaa', 'bbbbbbbbbb', 'jabjjjad'],
		   ['aab', 'aac', 'aacghgh', 'aabghgh']]

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


