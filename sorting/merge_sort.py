"""
This problem doesn't actually exist in hackerrank.
Using this as a basis for Merge Sort: Counting Inversions problem.

Input Format:
The first line contains an integer, d, denoting the number of datasets. 
The 2d subsequent lines describe each respective dataset over two lines:

The first line contains an integer, n, denoting the number of elements
in the dataset.
The second line contains n space-separated integers describing the
respective values of arr_0, arr_1, ..., arr_n-1.
"""


d = 2 # number of datasets
in_str = ['5', '1 1 1 2 2', '5', '2 1 3 1 2']

for i in range(d):
	inp = in_str.pop(0)
	n = int(inp.strip())

	inp = in_str.pop(0)
	arr = [int(temp) for temp in inp.strip().split(' ')]

	print('n: {0}  arr: {1}'.format(n, arr))



