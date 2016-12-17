"""
Input Format:
The first line contains a single integer, n, denoting the number
of integers in the data stream.
Each line i of the n subsequent lines contains an integer, a_i,
to be added to your list.

Output Format:
After each new integer is added to the list, print the list's
updated median on a new line as a single double-precision number
scaled to  decimal place (i.e., 12.3 format).
"""


import bisect


num_list = []
count = 0


def insert_and_find_median(x):
	global count
	bisect.insort(num_list, x)
	count += 1
	return calc_median()



def calc_median():
	if (count % 2 == 0):
		right = count // 2
		left = right - 1
		median = (num_list[left] + num_list[right]) / 2
	else:
		center = count // 2
		median = num_list[center]

	return median


# n = int(input().strip())
n = 6
in_str1 = [12, 4, 5, 3, 8, 7]


for i in range(n):
	# a_i = int(input().strip())
	a_i = in_str1[i]
	median = insert_and_find_median(a_i)
	print('{0:.1f}'.format(median))


