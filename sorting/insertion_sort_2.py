"""
In this challenge, don't print every time you move an element.
Instead, print the array after each iteration of the insertion-sort,
i.e., whenever the next element is placed at its correct position.

Since the array composed of just the first element is already "sorted",
begin printing from the second element and on.

Input Format:
s - the size of the array
ar - a list of numbers that makes up the array

Output Format:
On each line, output the entire array at every iteration.
"""


def insertion_sort(arr):
	# stuff here
	print(*arr, sep=' ')









# s = int(input().strip())
# arr = [int(temp) for temp in input().split(' ')]

s = 6
arr_str = '1 4 3 5 6 2'
arr = [int(temp) for temp in arr_str.split(' ')]

insertion_sort(arr)

