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
	half_1 = list_of_nums[:half]
	half_2 = list_of_nums[half:]    # second half could be longer

	if half > 1:
		half_1 = merge_sort(half_1)
		half_2 = merge_sort(half_2)

	sorted_list = []
	half_1_item = None
	half_2_item = None
	done = False

	while not done:
		if (len(half_1) <= 0) or (len(half_2) <= 0):
			done = True
		else:
			if half_1_item is None:
				half_1_item = half_1.pop(0)
			if half_2_item is None:
				half_2_item = half_2.pop(0)

			if half_1_item < half_2_item:
				sorted_list.append(half_1_item)
				half_1_item = None
			else:
				sorted_list.append(half_2_item)
				half_2_item = None

	# if one of the list still has items in it
	if len(half_1) > 0:
		sorted_list.extend(half_1)
	elif len(half_2) > 0:
		sorted_list.extend(half_2)

	return sorted_list


def merge(left, right):
	merged = []

	return merged



in_str = '10 5 2 7 4 9 12 1 8 6 11 3'

arr = [int(temp) for temp in in_str.strip().split(' ')]
sorted = merge_sort(arr)
print(sorted)

