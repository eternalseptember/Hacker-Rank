"""
Input Format:
The first line contains an integer, d, denoting the number of datasets. 
The 2d subsequent lines describe each respective dataset over two lines:

The first line contains an integer, n, denoting the number of elements
in the dataset.
The second line contains n space-separated integers describing the
respective values of arr_0, arr_1, ..., arr_n-1.
"""


def count_inversions(size, arr):
	for j in range(size):
		for i in range(j):
			# count inversions here?
			# inversion if arr_i > arr_j
	return arr



d = 2 # number of datasets
	  # expected answer: 0 4
in_str = ['5', '1 1 1 2 2', '5', '2 1 3 1 2']

for i in range(d):
	inp = in_str.pop(0)
	n = int(inp.strip())
	# n = int(input().strip())

	inp = in_str.pop(0)
	arr = [int(temp) for temp in inp.strip().split(' ')]
	# arr = list(map(int, input().strip().split(' ')))

	inversions = count_inversions(n, arr)
	print(inversions)



