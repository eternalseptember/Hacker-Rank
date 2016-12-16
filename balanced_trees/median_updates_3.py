"""
Yet another implementation of median_updates.
"""


import bisect


num_list = []
count = 0

def median_update(op, x):
	global count
	if op == 'a':
		bisect.insort(num_list, x)
		count += 1
		return calc_median()
	else:
		ind = search_index(num_list, x)
		if (ind == -1):
			return None
		else:
			del num_list[ind]
			count -= 1

			if count <= 0:
				return None
			else:
				return calc_median()


def search_index(num_list, val):
	pos = bisect.bisect_left(num_list, val)
	# The index of a list item is the insertion point.
	# If the pos == count, then the insertion point is at the end of the list,
	# which means the item is not in the list.
	# If the pos == 0, then the insertion point is at the beginning of the list.
	if (pos != count) and (num_list[pos] == val):
		return pos
	else:
		return -1


def calc_median():
	global count

	if (count % 2 == 0):
		right = count // 2
		left = right - 1
		median = (num_list[left] + num_list[right]) / 2
	else:
		center = count // 2
		median = num_list[center]

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
