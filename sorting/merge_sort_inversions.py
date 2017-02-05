"""
Input Format:
The first line contains an integer, d, denoting the number of datasets.
The 2d subsequent lines describe each respective dataset over two lines:

The first line contains an integer, n, denoting the number of elements
in the dataset.
The second line contains n space-separated integers describing the
respective values of arr_0, arr_1, ..., arr_n-1.
"""


def count_inversions(arr):
	inv, sorted_arr = sort_and_count(arr)
	return inv


def sort_and_count(list_of_nums):
	length = len(list_of_nums)
	if length <= 1:
		return 0, list_of_nums

	# setting up recursion
	half = length // 2
	left = list_of_nums[:half]
	right = list_of_nums[half:]  # second half could be longer

	left_inv, left = sort_and_count(left)
	right_inv, right = sort_and_count(right)
	merge_inv, merged = merge_and_count(left, right)
	inv_total = left_inv + right_inv + merge_inv

	return inv_total, merged


def merge_and_count(left, right):
	merged = []

	left_size = len(left)
	right_size = len(right)
	left_index = 0
	right_index = 0
	inv = 0

	while (left_index < left_size) and (right_index < right_size):
		if left[left_index] <= right[right_index]:
			merged.append(left[left_index])
			left_index += 1
		else:
			merged.append(right[right_index])
			right_index += 1
			inv += len(left[left_index:])

	if left_index == left_size:
		merged.extend(right[right_index:])
	elif right_index == right_size:
		merged.extend(left[left_index:])

	return inv, merged



# d = int(input().strip())
"""
d = 2 # number of datasets
	  # expected answer: 0 4
in_str = ['5', '1 1 1 2 2', '5', '2 1 3 1 2']
"""

d = 3 # number of datasets
	  # expected answer: 0 4 3
in_str = ['5', '1 1 1 2 2', '5', '2 1 3 1 2', '5', '2 4 1 3 5']

for i in range(d):
	inp = in_str.pop(0)
	n = int(inp.strip())
	# n = int(input().strip())

	inp = in_str.pop(0)
	arr = [int(temp) for temp in inp.strip().split(' ')]
	# arr = list(map(int, input().strip().split(' ')))

	inversions = count_inversions(arr)
	print(inversions)

	#inversions, sorted_arr = count_inversions(arr)
	#print('{0}  {1}'.format(inversions, sorted_arr))

