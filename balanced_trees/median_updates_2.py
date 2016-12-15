"""
Alternate implementation of median_updates.
"""


from collections import Counter


# max_heap on the left contains the smaller half
# min_heap on the right contains the larger half
max_heap = Counter()
min_heap = Counter()


def median_update(op, x):
	max_size = sum(max_heap.values())
	min_size = sum(min_heap.values())

	if op == 'a':
		# print('add: {0}'.format(x))
		if (max_size == 0) and (min_size == 0):
			# First item: put it in max_heap
			max_heap[x] += 1

		elif (min_size == 0) and (x < sorted(max_heap)[-1]):
			# Second item, scenario 1:
			# transfer first item from max_heap to min_heap
			transfer = sorted(max_heap)[-1]
			min_heap[transfer] += 1
			del max_heap[transfer]

			# then insert item in max_heap
			max_heap[x] += 1

		elif (min_size == 0) and (x >= sorted(max_heap)[-1]):
			# Second item, scenario 2: put it in min_heap
			min_heap[x] += 1

		else:
			# Third and after...
			if x < sorted(max_heap)[-1]:
				max_heap[x] += 1
			else:
				min_heap[x] += 1

		rebalance_heaps()
		calc_median()
	else:
		# print('remove: {0}'.format(x))
		found = False

		if (max_size > 0) and (x <= sorted(max_heap)[-1]):
			# look in max_heap
			if max_heap[x] > 0:
				found = True
				max_heap[x] -= 1

				if max_heap[x] == 0:
					del max_heap[x]

		if (min_size > 0) and (x >= sorted(min_heap)[0]) and (found is False):
			# look in min_heap
			if min_heap[x] > 0:
				found = True
				min_heap[x] -= 1

				if min_heap[x] == 0:
					del min_heap[x]

		# If the value is not in the list, print 'Wrong!'
		# If the list is empty after removal, print 'Wrong!';
		# otherwise, print the median.
		max_size = sum(max_heap.values())
		min_size = sum(min_heap.values())
		if found is False:
			print('Wrong!')
		elif (max_size == 0) and (min_size == 0):
			print('Wrong!')
		else:
			rebalance_heaps()
			calc_median()


def rebalance_heaps():
	max_size = sum(max_heap.values())
	min_size = sum(min_heap.values())
	diff = abs(max_size - min_size)

	if diff > 1:
		if min_size > max_size:
			# move elements from min heap to max heap
			transfer = sorted(min_heap)[0]
			min_heap[transfer] -= 1
			max_heap[transfer] += 1

			if min_heap[transfer] == 0:
				del min_heap[transfer]

		else:
			# move elements from max heap to min heap
			transfer = sorted(max_heap)[-1]
			max_heap[transfer] -= 1
			min_heap[transfer] += 1

			if max_heap[transfer] == 0:
				del max_heap[transfer]


def calc_median():
	max_size = sum(max_heap.values())
	min_size = sum(min_heap.values())

	if max_size == min_size:
		median = (sorted(min_heap)[0] + sorted(max_heap)[-1]) / 2
	else:
		if max_size < min_size:
			median = sorted(min_heap)[0]
		else:
			median = sorted(max_heap)[-1]

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
