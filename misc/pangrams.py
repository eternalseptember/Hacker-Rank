"""
Pangrams are sentences constructed by using every letter
of the alphabet at least once.

Input Format:
Input consists of a string.

Output Format:
Output a line containing pangram if s is a pangram,
otherwise output not pangram.
"""


def is_pangram(str):
	ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
	ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	for i in range(len(ascii_lowercase)):
		lower = ascii_lowercase[i]
		upper = ascii_uppercase[i]

		if (lower in str) or (upper in str):
			continue
		else:
			print('not pangram')
			return False

	print('pangram')
	return True



# str = input().strip()
# is_pangram(str)

str_in = ['We promptly judged antique ivory buckles for the next prize', 'We promptly judged antique ivory buckles for the prize']

for i in str_in:
	is_pangram(i)

