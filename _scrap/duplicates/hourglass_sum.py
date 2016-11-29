def calculate_hourglass_sum(arr, x, y):
	top_row = arr[x][y] + arr[x][y+1] + arr[x][y+2]
	mid_row = arr[x+1][y+1]
	bot_row = arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
	#print('top: {1}\nmid: {1}\nbot: {2}'.format(top_row, mid_row, bot_row))
	return top_row + mid_row + bot_row




# arr[row_num][col_num]
# arr[0][0] = 1
# arr[0][1] = 1
# arr[1][0] = 0
arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]


highest_sum = 0
for y in range(4):		# row[][y]
	for x in range(4):	# row[x][]
		this_sum = calculate_hourglass_sum(arr, x, y)
		if ((x == 0) and (y == 0)):
			highest_sum = this_sum
		elif this_sum > highest_sum:
			highest_sum = this_sum


print(highest_sum)
