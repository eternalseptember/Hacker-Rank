"""
Yet another implementation of median_updates.
"""


import bisect


num_list = []
count = 0

def median_update(op, x):
	global count
	if op == 'a':
		# print('add: {0}'.format(x))
		bisect.insort(num_list, x)
		count += 1
		return calc_median()
	else:
		# print('remove: {0}'.format(x))
		try:
			num_list.remove(x)
			count -= 1
		except ValueError:
			return None

		if count <= 0:
			return None
		else:
			return calc_median()


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
