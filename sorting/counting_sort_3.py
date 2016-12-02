"""
Challenge:
You will be given a list that contains both integers and strings.
In this challenge you just care about the integers. For every
value i from 0 to 99, can you output L, the number of elements
that are less than or equal to i?

Input Format:
- n, the size of the list ar.
- n lines follow, each containing an integer x and a string s.

Output Format:
Output L for all numbers from 0 to 99 (inclusive).
"""


# n = int(input().strip())
counts = [0] * 100
total = 0

n = 10
in_str1 = ['4 that', '3 be', '0 to', '1 be', '5 question', '1 or', '2 not', '4 is', '2 to', '4 the']


for i in range(n):
	# x, s = input().strip().split(' ')
	x, s = in_str1[i].strip().split(' ')
	counts[int(x)] += 1


for num in counts:
	total += num
	print(total, end=' ')








