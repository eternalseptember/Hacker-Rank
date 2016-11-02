"""
Insert element into sorted list
Given a sorted list with an unsorted number e in the rightmost cell,
can you write some simple code to insert e into the array so that it
remains sorted?

Print the array every time a value is shifted in the array until the
array is fully sorted. The goal of this challenge is to follow the
correct order of insertion sort.


Input Format:
There will be two lines of input:
1. the size of the array
2. the unsorted array of integers

Output Format:
On each line, output the entire array every time an item is shifted in it.
"""


def insertion_sort(arr, size):
	sorting = arr[:]
	e = sorting[-1]

	for i in range((size - 2), -2, -1):
		if i == -1:
			sorting[0] = e
		elif sorting[i] > e:
			sorting[i + 1] = sorting[i]
		else:
			sorting[i + 1] = e
			print(*sorting, sep=' ')
			break

		print(*sorting, sep=' ')



in_1 = ['5', '10']
in_2 = ['2 4 6 8 3', '2 3 4 5 6 7 8 9 10 1']

# size = int(input().strip())
# unsorted = [int(temp) for temp in input().split(' ')]

for i in range(len(in_1)):
	in_1_str = in_1[i]
	in_2_str = in_2[i]

	size = int(in_1_str.strip())
	unsorted = [int(temp) for temp in in_2_str.split(' ')]

	insertion_sort(unsorted, size)
	print()
