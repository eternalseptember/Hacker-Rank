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
	# stuff here
	print(*arr, sep=' ')






# n = input().strip()
# arr = [int(temp) for temp in input().split(' ')]


n = 7
in_1 = '1 3 9 8 2 7 5'
arr = [int(temp) for temp in in_1.split(' ')]

quick_sort_inplace(arr)



