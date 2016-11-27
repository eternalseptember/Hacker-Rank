"""
Input Format:
The first line contains two space separated integers, N and Q.
The next line contains N space separated integers representing
the initial pile of plates, i.e., A0. The leftmost value
represents the bottom plate of the pile.

Output Format:
Output N lines. Each line contains a number written on the plate.
Printing should be done in the order defined above.
"""


def stack_plates(pile, iterations):
	return pile




# N, Q = (int(temp) for temp in input().strip().split(' '))
# A0 = [int(temp) for temp in input().strip().split(' ')]

in_1 = '5 1'
in_2 = '3 4 7 6 5'

N, Q = (int(temp) for temp in in_1.strip().split(' '))
A0 = [int(temp) for temp in in_2.strip().split(' ')]

new_stack = stack_plates(A0, Q)
for i in new_stack:
	print(i)



