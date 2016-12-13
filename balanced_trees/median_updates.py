"""
Input:
The first line is an integer, N, that indicates the number of
operations. Each of the next N lines is either a x or r x.
a x indicates that x is added to the set, and
r x indicates that x is removed from the set.

Output:
For each operation: If the operation is add, output the median
after adding x in a single line. If the operation is remove and
the number x is not in the list, output Wrong! in a single line.
If the operation is remove and the number x is in the list,
output the median after deleting x in a single line. (If the
result is an integer DO NOT output decimal point. And if the
result is a real number, DO NOT output trailing 0s.)
"""

import heapq


def _heappush_max(heap, item):
	heap.append(item)
	heapq._siftdown_max(heap, 0, len(heap) - 1)


# max_heap on the left contains the smaller half
# min_heap on the right contains the larger half
max_heap = []
min_heap = []
heapq._heapify_max(max_heap)
heapq.heapify(min_heap)


def median_update(op, x):
	if op == 'a':
		# print('add: {0}'.format(x))
		max_size = len(max_heap)
		min_size = len(min_heap)

		if (max_size == 0) and (min_size == 0):
			# First item
			_heappush_max(max_heap, x)
		elif (min_size == 0) and (x < max_heap[0]):
			# Second item, scenario 1:
			# transfer item from max_heap to min_heap
			transfer = heapq._heappop_max(max_heap)
			heapq.heappush(min_heap, transfer)
			# insert item in max_heap
			_heappush_max(max_heap, x)
		elif (min_size == 0) and (x >= max_heap[0]):
			# Second item, scenario 2:
			heapq.heappush(min_heap, x)
		else:
			# Third and after...
			if x < max_heap[0]:
				_heappush_max(max_heap, x)
			else:
				heapq.heappush(min_heap, x)

		rebalance_heaps()
		calc_median()

	else:
		# print('remove: {0}'.format(x))
		# Remove the item from list.
		found = False
		if (len(max_heap) > 0) and (x <= max_heap[0]):
			# look in max_heap
			try:
				max_heap.remove(x)
				found = True
			except (ValueError, IndexError):
				found = False
		if (len(min_heap) > 0) and (x >= min_heap[0]) and (found is False):
			# look in min_heap
			try:
				min_heap.remove(x)
				found = True
			except (ValueError, IndexError):
				found = False

		# If the value is not in the list, print 'Wrong!'
		# If the list is empty after removal, print 'Wrong!';
		# otherwise, print the median.
		max_size = len(max_heap)
		min_size = len(min_heap)
		if found is False:
			print('Wrong!')
		elif (max_size == 0) and (min_size == 0):
			print('Wrong!')
		else:
			rebalance_heaps()
			calc_median()


def rebalance_heaps():
	max_size = len(max_heap)
	min_size = len(min_heap)
	diff = abs(max_size - min_size)

	if diff > 1:
		if min_size > max_size:
			# move elements from min heap to max heap
			transfer = heapq.heappop(min_heap)
			_heappush_max(max_heap, transfer)
		else:
			# move elements from max heap to min heap
			transfer = heapq._heappop_max(max_heap)
			heapq.heappush(min_heap, transfer)


def calc_median():
	max_size = len(max_heap)
	min_size = len(min_heap)
	if max_size == min_size:
		median = (min_heap[0] + max_heap[0]) / 2
	else:
		if max_size < min_size:
			median = min_heap[0]
		else:
			median = max_heap[0]

	print_median(median)


def print_median(i):
	if (type(i) == int) or (int(i) == i):
		print(int(i))
	else:
		print('%.1f' % i)


# N = int(input().strip())

N = 7
in_str1 = ['r 1', 'a 1', 'a 2', 'a 1', 'r 1', 'r 2', 'r 1']

for i in range(N):
	# op, x = input().strip().split(' ')
	op, x = in_str1[i].strip().split(' ')
	median_update(op, int(x))

# should be: Wrong!, 1, 1.5, 1, 1.5, 1, Wrong!



