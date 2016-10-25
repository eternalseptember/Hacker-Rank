"""
Given n strings of brackets, determine whether each sequence of
brackets is balanced. If a string is balanced, print YES on a new
line; otherwise, print NO on a new line.

Input Format:
The first line contains a single integer, n, denoting the number of
strings. Each line i of the n subsequent lines consists of a single
string, s, denoting a sequence of brackets.
"""

def is_balanced(str):
	#




t = 3
in_str = ['{[()]}', '{[(])}', '{{[[(())]]}}']


# t = int(input().strip())
for i in range(t):
	# s = input().strip()
	s = in_str[i].strip()

	if is_balanced(str):
		print('YES')
	else:
		print('NO')

