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
	stack = []
	open_brackets = ['{', '(', '[']

	for char in str:
		if char in open_brackets:
			stack.append(char)
		else:
			if len(stack)> 0:
				open_bracket = stack.pop()
				if (open_bracket == '{') and (char == '}'):
					continue
				elif (open_bracket == '(') and (char == ')'):
					continue
				elif (open_bracket == '[') and (char == ']'):
					continue
				else:
					return False
			else:
				return False

	# after going through all of the characters in the string...
	if len(stack) == 0:
		return True
	else:
		return False


t = 3
in_str = ['{[()]}', '{[(])}', '{{[[(())]]}}']


# t = int(input().strip())
for i in range(t):
	# s = input().strip()
	s = in_str[i].strip()

	if is_balanced(s):
		print('YES')
	else:
		print('NO')

