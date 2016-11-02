"""
Input:
First line contains an integer n, denoting the number of
elements in array a.
Second line contains n space-separated integers describing
a, where the i-th integer is a[i].

Output:
1. "Array is sorted in numSwaps swaps."
2. "First Element: firstElement"
3. "Last Element: lastElement"
"""


def bubble_sort(size, array):
	totalSwaps = 0

	for i in range(size):
		swap = False

		for j in range(size - 1):
			if a[j] > a[j + 1]:
				swap = True
				a[j], a[j + 1] = a[j + 1], a[j]
				totalSwaps += 1

		if swap is False:
			break

	return array, totalSwaps


# n = int(input().strip())
# a = [int(a_temp) for a_temp in input().strip().split(' ')]

n = 3
str = '3 2 1'
a = [int(a_temp) for a_temp in str.strip().split(' ')]

a, numSwaps = bubble_sort(n, a)

print('Array is sorted in {0} swaps.'.format(numSwaps))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[n - 1]))
