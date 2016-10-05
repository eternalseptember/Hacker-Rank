"""
Given an array of n integers and a number, d, perform d left
rotations on the array. Then print the updated array as a
single line of space-separated integers.

Input Format:
The first line contains two space-separated integers denoting
the respective values of n (the number of integers) and d
(thenumber of left rotations you must perform).
The second line contains  space-separated integers describing
the respective elements of the array's initial state.
"""


def left_rotate_array(arr, rot):
	size = len(arr)
	rotated = []

	index = rot
	for i in range(size):
		rotated.append(arr[index])

		index += 1
		if index >= size:
			index = 0

	return rotated

# str = input()
str = '5 4'
arr_size, rot = str.split(' ')
arr_size = int(arr_size)
rot = int(rot)

# arr_input = input()
arr_input = '1 2 3 4 5'
arr = [int(arr_temp) for arr_temp in arr_input.split(' ')]

newArr = left_rotate_array(arr, rot)
for i in range(arr_size):
	print(newArr[i], end=' ')


