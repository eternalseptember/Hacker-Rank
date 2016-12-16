"""
Alternate implementation of median_updates.
"""


from collections import Counter


# max_heap on the left contains the smaller half
# min_heap on the right contains the larger half
max_heap = Counter()
min_heap = Counter()
max_size = 0
min_size = 0


def median_update(op, x):
	global max_size
	global min_size
	if max_size > 0:
		max_heap_top = sorted(max_heap)[-1]
	if min_size > 0:
		min_heap_top = sorted(min_heap)[0]

	if op == 'a':
		# print('add: {0}'.format(x))
		if (max_size == 0) and (min_size == 0):
			# First item: put it in max_heap
			max_heap[x] += 1
			max_size += 1

		elif (min_size == 0) and (x < max_heap_top):
			# Second item, scenario 1:
			# transfer first item from max_heap to min_heap
			del max_heap[max_heap_top]
			min_heap[max_heap_top] += 1
			min_size += 1

			# then insert item in max_heap
			max_heap[x] += 1

		elif (min_size == 0) and (x >= max_heap_top):
			# Second item, scenario 2: put it in min_heap
			min_heap[x] += 1
			min_size += 1

		else:
			# Third and after...
			if x < max_heap_top:
				max_heap[x] += 1
				max_size += 1
			else:
				min_heap[x] += 1
				min_size += 1

		rebalance_heaps()
		return calc_median()
	else:
		# print('remove: {0}'.format(x))
		found = False

		if (max_size > 0) and (x <= max_heap_top):
			# look in max_heap
			if max_heap[x] > 0:
				found = True
				max_heap[x] -= 1
				max_size -= 1

				if max_heap[x] == 0:
					del max_heap[x]

		if (min_size > 0) and (x >= min_heap_top) and (found is False):
			# look in min_heap
			if min_heap[x] > 0:
				found = True
				min_heap[x] -= 1
				min_size -= 1

				if min_heap[x] == 0:
					del min_heap[x]

		# If the value is not in the list, print 'Wrong!'
		# If the list is empty after removal, print 'Wrong!';
		# otherwise, print the median.
		if found is False:
			return None
		elif (max_size == 0) and (min_size == 0):
			return None
		else:
			rebalance_heaps()
			return calc_median()


def rebalance_heaps():
	global max_size
	global min_size
	diff = abs(max_size - min_size)

	if diff > 1:
		if min_size > max_size:
			# move elements from min heap to max heap
			transfer = sorted(min_heap)[0]
			min_heap[transfer] -= 1
			max_heap[transfer] += 1

			min_size -= 1
			max_size += 1

			if min_heap[transfer] == 0:
				del min_heap[transfer]

		else:
			# move elements from max heap to min heap
			transfer = sorted(max_heap)[-1]
			max_heap[transfer] -= 1
			min_heap[transfer] += 1

			max_size -= 1
			min_size += 1

			if max_heap[transfer] == 0:
				del max_heap[transfer]


def calc_median():
	global max_size
	global min_size

	if max_size == min_size:
		median = (sorted(min_heap)[0] + sorted(max_heap)[-1]) / 2
	else:
		if max_size < min_size:
			median = sorted(min_heap)[0]
		else:
			median = sorted(max_heap)[-1]

	return median


def print_median(i):
	if i is None:
		print('Wrong!')
	elif (type(i) == int) or (int(i) == i):
		print(int(i))
	else:
		print('%.1f' % i)



# N = int(input().strip())

N = 7
in_str1 = ['r 1', 'a 1', 'a 2', 'a 1', 'r 1', 'r 2', 'r 1']

for i in range(N):
	# op, x = input().strip().split(' ')
	op, x = in_str1[i].strip().split(' ')
	median = median_update(op, int(x))
	print_median(median)

# should be: Wrong!, 1, 1.5, 1, 1.5, 1, Wrong!
