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


def quick_sort_inplace(arr):
	pivot = partition(arr, 0, len(arr)-1)
	#left_pivot = partition(arr, 0, pivot-1)
	#right_pivot = partition(arr, pivot+1, len(arr)-1)


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
			# arr[i] < pivot
			if larger_partition_index is not None:
				arr[i], arr[larger_partition_index] = arr[larger_partition_index], arr[i]
				larger_partition_index += 1

	if larger_partition_index is not None:
		arr[pivot_index], arr[larger_partition_index] = arr[larger_partition_index], arr[pivot_index]

	print(*arr, sep=' ')

	left = partition(arr, beg_index, larger_partition_index-1)
	right = partition(arr, larger_partition_index+1, pivot_index)

	return larger_partition_index





# n = input().strip()
# arr = [int(temp) for temp in input().split(' ')]


n = 7
in_1 = '1 3 9 8 2 7 5'
arr = [int(temp) for temp in in_1.split(' ')]

quick_sort_inplace(arr)



