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
	# return shifts
	return len(arr)


def quick_sort_swaps(arr):
	# return swaps
	return len(arr)



n = 7
in_str1 = '1 3 9 8 2 7 5'
arr = [int(temp) for temp in in_str1.strip().split(' ')]

# n = int(input().strip())
# arr = [int(temp) for temp in input().strip().split(' ')]

D = insertion_sort_shifts(arr) - quick_sort_swaps(arr)
print(D)

