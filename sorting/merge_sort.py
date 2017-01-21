"""
This problem doesn't actually exist in hackerrank, but there is a
HR video on this topic from Gayle Laakmann McDowell.
Using this as a basis for Merge Sort: Counting Inversions problem.
"""


def merge_sort(list_of_nums):
	length = len(list_of_nums)
	if length <= 1:
		return list_of_nums

	# setting up recursion
	half = length // 2
	left = list_of_nums[:half]
	right = list_of_nums[half:]    # second half could be longer

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)


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



in_str = '10 5 2 7 4 9 12 1 8 6 11 3'

arr = [int(temp) for temp in in_str.strip().split(' ')]
sorted = merge_sort(arr)
print(sorted)

