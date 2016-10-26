"""
There are N buildings in a certain two-dimensional landscape. Each
building has a height given by h_i, i element of [1, N]. If you join
K adjacent buildings, they will form a solid rectangle of area
K x min(h_i, h_i+1, ..., h_i+k-1).

Given N buildings, find the greatest such solid area formed by
consecutive buildings.

Input Format:
The first line contains N, the number of buildings altogether.
The second line contains N space-separated integers, each
representing the height of a building.

Output Format:
One integer representing the maximum area of rectangle formed.
"""


def find_largest_rect(n, height_list):
	# apparently all width is 1
	heights = []
	indexes = []
	max_area = 0

	# iterates through the original histogram
	for i in range(n):
		current_bar = height_list[i]
		if (len(heights) == 0) or (heights[-1] <= current_bar):
			heights.append(current_bar)
			indexes.append(i)
		else:
			# while current_bar is greater than the top of the stack
			# pop from stack and calculate area
			while (heights[-1] > current_bar):
				top_bar = heights.pop()
				indexes.pop()

				if len(heights) == 0:
					area = top_bar * i
				else:
					area = top_bar * (i - indexes[-1] - 1)

				if area > max_area:
					max_area = area

				if len(heights) == 0:
					break

			# after stack popping and area calculation
			heights.append(current_bar)
			indexes.append(i)

	# iterates through the stored histogram
	while (len(heights) > 0):
		top_bar = heights.pop()
		indexes.pop()

		if len(heights) == 0:
			area = top_bar * n
		else:
			area = top_bar * (n - indexes[-1] - 1)

		if area > max_area:
			max_area = area


	return max_area


# n = int(input().strip())
# heights = [int(temp) for temp in input().strip().split(' ')]

n = [5, 5, 7, 10]
in_str = ['1 2 3 4 5', '5 3 1 2 3', '6 2 5 4 5 1 6',
	'8979 4570 6436 5083 7780 3269 5400 7579 2324 2116']

# answers should be 9, 6, 12, 26152
for i in range(len(n)):
	heights = [int(temp) for temp in in_str[i].strip().split(' ')]
	max_height = find_largest_rect(n[i], heights)
	print(max_height)
