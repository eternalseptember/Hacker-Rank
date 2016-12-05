"""
Challenge:
Given a list of unsorted integers, A = {a1, a2, ..., aN},
can you find the pair of elements that have the smallest
absolute difference between them? If there are multiple
pairs, find them all.

Input Format:
The first line of input contains a single integer, N,
representing the length of array A.
In the second line, there are N space-separated integers,
a1, a2, ..., aN, representing the elements of array A.

Output Format:
Output the pairs of elements with the smallest difference.
If there are multiple pairs, output all of them in ascending
order, all on the same line (consecutively) with just a
single space between each pair of numbers. If there's a
number which lies in two pair, print it two times (see the
sample case #3 for explanation).
"""


def smallest_difference(arr):
	# return pairs
	print(arr)




# N = int(input().strip())
# A = [int(temp) for temp in input().strip().split(' ')]
# smallest_difference(A)


# Test case 1: -20 30
# Test case 2: -520 -470 -20 30
# Test case 3: 2 3 3 4 4 5
N = 10, 12, 4
in_str1 = ['-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854',
'-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 ',
'5 4 3 2']

for str in in_str1:
	A = [int(temp) for temp in str.strip().split(' ')]
	smallest_difference(A)



