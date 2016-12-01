"""
Input:
The first line is an integer, N, that indicates the number of
operations. Each of the next N lines is either a x or r x.
a x indicates that x is added to the set, and
r x indicates that x is removed from the set.

Output:
For each operation: If the operation is add, output the median
after adding x in a single line. If the operation is remove and
the number x is not in the list, output Wrong! in a single line.
If the operation is remove and the number x is in the list,
output the median after deleting x in a single line. (If the
result is an integer DO NOT output decimal point. And if the
result is a real number, DO NOT output trailing 0s.)
"""


import heaqp





def median(op, x):
	"""
	if op == 'a':
		print('add: {0}'.format(x))
	else:
		# try... catch?
		print('remove: {0}'.format(x))
	"""

	if (type(i) == int) or (int(i) == i):
		print(int(i))
	else:
		print('%.1f' % i)


# N = int(input().strip())


N = 7  
in_str1 = ['r 1', 'a 1', 'a 2', 'a 1', 'r 1', 'r 2', 'r 1']


for i in range(N):
	# op, x = input().strip().split(' ')
	op, x = in_str1[i].strip().split(' ')
	median(op, int(x))

# should be: Wrong!, 1, 1.5, 1, 1.5, 1, Wrong!



