"""
Hourglass sum
Calculate the hourglass sum for every hourglass in A, then print
the maximum hourglass sum.

Input Format:
There are  lines of input, where each line contains 6 space-separated
integers describing 2D Array A; every value in A will be in the
inclusive range of -9 to 9.

"""

arr = []
for arr_i in range(6):
	arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	arr.append(arr_t)


def calculate_hourglass_sum(arr, x, y):
	top_row = arr[x][y] + arr[x][y+1] + arr[x][y+2]
	mid_row = arr[x+1][y+1]
	bot_row = arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
	return top_row + mid_row + bot_row


highest_sum = 0
for y in range(4):		# row[][y]
	for x in range(4):  # row[x][]
		this_sum = calculate_hourglass_sum(arr, x, y)
		if ((x == 0) and (y == 0)):
			highest_sum = this_sum
		elif this_sum > highest_sum:
			highest_sum = this_sum

print(highest_sum)
