"""
Create an in-place version of Quicksort. You need to follow Lomuto
Partitioning method.

Input Format:
There will be two lines of input:
n - the size of the array
ar - the n numbers of the array
There are no duplicate numbers.

Output Format:
Print the entire array on a new line at the end of every partitioning method.
"""


def partition(arr, beg_index, pivot_index):
	size = len(arr[beg_index:pivot_index + 1])
	if size <= 1:
		return None

	pivot = arr[pivot_index]
	larger_partition_index = None

	for i in range(beg_index, pivot_index):
		if arr[i] > pivot:
			if larger_partition_index is None:
				larger_partition_index = i
		else:
			if larger_partition_index is not None:
				arr[i], arr[larger_partition_index] = arr[larger_partition_index], arr[i]
				larger_partition_index += 1

	if larger_partition_index is not None:
		arr[pivot_index], arr[larger_partition_index] = arr[larger_partition_index], arr[pivot_index]

	print(*arr, sep=' ')

	if larger_partition_index is None:
		# the pivot item is the largest item
		# so redo this partition, but moving the pivot to the left one position
		partition(arr, beg_index, pivot_index - 1)

	if larger_partition_index is not None:
		partition(arr, beg_index, larger_partition_index - 1)
		partition(arr, larger_partition_index + 1, pivot_index)

	return larger_partition_index





# n = input().strip()
# arr = [int(temp) for temp in input().split(' ')]


n = [7, 9]
in_1 = ['1 3 9 8 2 7 5', '9 8 6 7 3 5 4 1 2']

for i in range(len(n)):
	arr = [int(temp) for temp in in_1[i].split(' ')]
	partition(arr, 0, len(arr) - 1)
	print()

"""
First case:
1 3 2 5 9 7 8
1 2 3 5 9 7 8
1 2 3 5 7 8 9

Second case:
1 2 6 7 3 5 4 9 8
1 2 6 7 3 5 4 8 9
1 2 3 4 6 5 7 8 9
1 2 3 4 6 5 7 8 9
1 2 3 4 5 6 7 8 9
"""

