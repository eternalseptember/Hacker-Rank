"""
Note
Please maintain the original order of the elements in the left and right
partitions while partitioning around a pivot element.

For example: Partition about the first element for the array
A[] = {5, 8, 1, 3, 7, 9, 2} will be {1, 3, 2, 5, 8, 7, 9}

Input Format:
There will be two lines of input:
*  n - the size of the array
*  arr - the n numbers of the array
Each number is unique.

Output Format:
Print every partitioned sub-array on a new line.
"""


def quick_sort(arr):
	left, p, right = partition(arr)
	



	sorted_list = left + p + right
	print(*sorted_list, sep=' ')



def partition(arr):
	if (len(arr) <= 1):
		return None

	p = [arr.pop()]
	left = []
	right = []

	for i in arr:
		if i < p[0]:
			left.append(i)
		else:
			right.append(i)

	new_list = left + p + right
	print(*new_list, sep=' ')

	return left, p, right



#n = int(input().strip())
#arr = [int(temp) for temp in input.split(' ')]


n = 7
in_1 = '5 8 1 3 7 9 2'
arr = [int(temp) for temp in in_1.split(' ')]

partition(arr)
