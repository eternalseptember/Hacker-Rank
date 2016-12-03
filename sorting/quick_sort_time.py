"""
Please use Lomuto Partition for this challenge.

Input Format:
There will be two lines of input:
n - the size of the array
ar - n numbers that make up the array

Output Format:
Output one integer D, where
D = (insertion sort shifts) - (quicksort swaps)
"""


def insertion_sort_shifts(arr):
	shifts = 0
	length = len(arr)

	# The first element is already "sorted".
	# i is the unsorted element being compared.
	for i in range(1, length):
		# Iterate backwards through "sorted" elements.
		# j = i - 1 is the index for first sorted item.
		for j in range(i - 1, -1, -1):
			# Use j as index base because of the shift.
			# "j = i - 1" means "i = j + 1".
			if arr[j + 1] < arr[j]:
				arr[j + 1], arr[j] = arr[j], arr[j + 1]
				shifts += 1
			else:
				break

	return shifts


def quick_sort_swaps(arr, beg_index=0, pivot_index=None):
	# pivot_index should only be None for first invocation.
	# Recursive calls will supply pivot_index.
	if pivot_index is None:
		pivot_index = len(arr) - 1

	size = len(arr[beg_index:pivot_index + 1])

	if size <= 1:
		return 0

	pivot = arr[pivot_index]
	large_part_index = None
	swap = 0

	# 1. Sort and swap the body.
	for i in range(beg_index, pivot_index):
		if arr[i] > pivot:
			if large_part_index is None:
				large_part_index = i
		else:
			swap += 1
			if large_part_index is not None:
				arr[i], arr[large_part_index] = arr[large_part_index], arr[i]
				large_part_index += 1

	# 2. Then swap the pivot with the first item of the larger partition.
	if large_part_index is not None:
		arr[pivot_index], arr[large_part_index] = arr[large_part_index], arr[pivot_index]
		swap += 1

	# 2a. Unless the pivot was the largest item.
	# So partition again with the pivot point moved to the left once.
	else:
		sub_swap = quick_sort_swaps(arr, beg_index, pivot_index - 1)
		swap += sub_swap

	# 3. Now partition the larger and smaller halves.
	if large_part_index is not None:
		left_swap = quick_sort_swaps(arr, beg_index, large_part_index - 1)
		right_swap = quick_sort_swaps(arr, large_part_index + 1, pivot_index)
		swap += left_swap + right_swap

	return swap



n = 7
in_str1 = '1 3 9 8 2 7 5'
arr1 = [int(temp) for temp in in_str1.strip().split(' ')]

# n = int(input().strip())
# arr1 = [int(temp) for temp in input().strip().split(' ')]
arr2 = arr1[:]

D = insertion_sort_shifts(arr1) - quick_sort_swaps(arr2)
print(D)



