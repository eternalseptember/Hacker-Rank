"""
Input Format:
The first line contains n (the size of ar).
The second line contains  space-separated integers describing ar
(the unsorted array). The first integer (corresponding to ar[0])
is your pivot element, p.

Output Format:
On a single line, print the partitioned numbers (i.e.: the elements
in left, then the elements in equal, and then the elements in right).
Each integer should be separated by a single space.
"""


def quick_sort(arr):
	# stuff here
	p = arr[0]
	left = []
	equal = []
	right = []

	for i in arr:
		if i < p:
			left.append(i)
		elif i > p:
			right.append(i)
		else:
			equal.append(i)

	new_list = left + equal + right
	print(*new_list, sep=' ')




# n = int(input().strip())
# arr = [int(temp) for temp in input().split(' ')]

n = '5'
in_1 = '4 5 3 7 2'
arr = [int(temp) for temp in in_1.split(' ')]
# expected output: 3 2 4 5 7

quick_sort(arr)


