"""
This problem doesn't actually exist in hackerrank, but there is a
HR video on this topic from Gayle Laakmann McDowell.
Using this as a basis for Merge Sort: Counting Inversions problem.
"""


def merge_sort(list_of_nums):
	# stuff here
	return list_of_nums




in_str = '10 5 2 7 4 9 12 1 8 6 11 3'

arr = [int(temp) for temp in in_str.strip().split(' ')]
sorted = merge_sort(arr)
print(sorted)

