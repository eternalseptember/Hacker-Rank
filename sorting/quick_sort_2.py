"""
Note
Please maintain the original order of the elements in the left and right
partitions while partitioning around a pivot element.

For example: Partition about the first element for the array
A[]={5, 8, 1, 3, 7, 9, 2} will be {1, 3, 2, 5, 8, 7, 9}

Input Format:
There will be two lines of input:
*  n - the size of the array
*  arr - the n numbers of the array

Output Format:
Print every partitioned sub-array on a new line.
"""


def quick_sort(arr):
	for i in arr:
		print(i, end=' ')



#n = int(input().strip())
#arr = [int(temp) for temp in input.split(' ')]


n = 7
in_1 = '5 8 1 3 7 9 2'
arr = [int(temp) for temp in in_1.split(' ')]

quick_sort(arr)
