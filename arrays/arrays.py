"""
Given an array, A, of N integers, print each element in reverse
order as a single line of space-separated integers.

Input Format:
The first line contains an integer, N (the number of integers in A).
The second line contains N space-separated integers describing A.
"""


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.reverse()
for i in range(n):
	print(arr[i], end=' ')
