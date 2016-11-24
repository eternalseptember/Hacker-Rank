"""
Can you modify your previous Insertion Sort implementation
to keep track of the number of shifts it makes while sorting?

Input Format:
The first line contains N, the number of elements to be sorted.
The next line contains integers a[1], a[2], ..., a[N].

Output Format:
Output the number of shifts it takes to sort the array.
"""



def insertion_sort(arr, size):
	shifts = 0
	
	# unsorted subset i
	for i in range(1, size):
		# traverses through the sorted pile j
		for j in range(i - 1, -1, -1):
			if arr[j + 1] < arr[j]:
				arr[j + 1], arr[j] = arr[j], arr[j + 1]
				shifts += 1

	print(shifts)



# n = int(input().strip())
# arr = [int(temp) for temp in input().split(' ')]


n = 5
in_str = '2 1 3 1 2'
arr = [int(temp) for temp in in_str.split(' ')]

insertion_sort(arr, n)
