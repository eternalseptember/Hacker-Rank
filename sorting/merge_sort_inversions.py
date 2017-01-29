"""
Input Format:
The first line contains an integer, d, denoting the number of datasets. 
The 2d subsequent lines describe each respective dataset over two lines:

The first line contains an integer, n, denoting the number of elements
in the dataset.
The second line contains n space-separated integers describing the
respective values of arr_0, arr_1, ..., arr_n-1.
"""


def count_inversions(size, arr):
	inversions = 0
	for j in range(size):
		for i in range(j):
			if arr[i] > arr[j]:
				inversions += 1
	return inversions


def merge_sort(list_of_nums):
	length = len(list_of_nums)
	if length <= 1:
		return list_of_nums

	# setting up recursion
	half = length // 2
	left = list_of_nums[:half]
	right = list_of_nums[half:]  # second half could be longer

	left_inv, left = merge_sort(left)
	right_inv, right = merge_sort(right)
	merge_inv, merged = merge(left, right)
	inv_total = left_inv, right_inv, merge_inv

	return inv_total, merged


def merge(left, right):
	merged = []

	total_length = len(left) + len(right)
	left_item = None
	right_item = None

	for i in range(total_length):
		if (left_item is None) and (len(left) > 0):
			left_item = left.pop(0)
		if (right_item is None) and (len(right) > 0):
			right_item = right.pop(0)

		if (left_item is None):
			merged.append(right_item)
			right_item = None
		elif (right_item is None):
			merged.append(left_item)
			left_item = None
		else:
			if left_item < right_item:
				merged.append(left_item)
				left_item = None
			else:
				merged.append(right_item)
				right_item = None

	return merged




# d = int(input().strip())
d = 2 # number of datasets
	  # expected answer: 0 4
in_str = ['5', '1 1 1 2 2', '5', '2 1 3 1 2']

for i in range(d):
	inp = in_str.pop(0)
	n = int(inp.strip())
	# n = int(input().strip())

	inp = in_str.pop(0)
	arr = [int(temp) for temp in inp.strip().split(' ')]
	# arr = list(map(int, input().strip().split(' ')))

	inversions = count_inversions(n, arr)
	print(inversions)



