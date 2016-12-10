"""
Given a list of numbers, can you find the median?

Input Format:
There will be two lines of input:
n - the size of the array
arr - n numbers that makes up the array

Output Format:
Output one integer, the median.
"""


def find_median(arr):
	arr.sort()
	med = len(arr)//2
	return arr[med]


# n = int(input().strip())
# arr = [int(temp) for temp in input().strip().split(' ')]

# test case 1, expected answer: 3
n = 7
in_str1 = '0 1 2 4 6 5 3'

arr = [int(temp) for temp in in_str1.strip().split(' ')]

median = find_median(arr)
print(median)



