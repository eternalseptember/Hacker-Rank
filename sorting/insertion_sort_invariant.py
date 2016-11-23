"""
In the InsertionSort code below, there is an error.
Can you fix it? Print the array only once, when it
is fully sorted.
"""


def insertion_sort(l):
	for i in range(1, len(l)):
		j = i - 1
		key = l[i]
		while (j > 0) and (l[j] > key):
			l[j + 1] = l[j]
			j -= 1
		l[j + 1] = key


#m = int(input().strip())
#ar = [int(i) for i in input().strip().split()]

m = 6
in_str = '1 4 3 5 6 2'
ar = [int(i) for i in in_str.split()]

insertion_sort(ar)
print(" ".join(map(str, ar)))
