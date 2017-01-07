"""
Given a number of dollars, n, and a list of dollar values for m distinct
coins, C = {c_0, c_1, c_2, ..., c_m-1}, find and print the number of
different ways you can make change for n dollars if each coin is available
in an infinite quantity.

Input Format:
The first line contain two space-separated integers describing the respective
values of n and m.
The second line contains m space-separated integers describing the respective
values of c_0, c_1, ..., c_m-1, where each integer denotes the dollar value of
a distinct coin available in an infinite quantity.

Output Format:
Print a single integer denoting the number of ways we can make change for n
dollars using an infinite supply of our m types of coins.
"""


def make_change(total, num_of_coins, list_of_coins):
	list = [0 for i in range(total + 1)]

	# base case: one way to make change for 0 dollars
	list[0] = 1

	for coin in range(0, num_of_coins):
		for change in range(list_of_coins[coin], total+1):
			list[change] += list[change - list_of_coins[coin]]

	#print(list)
	return list[total]



"""
n, m = (int(x) for x in input().strip().split(' '))
list_of_coins = [int(x) for x in input().strip().split(' ')]
list_of_coins.sort()
ways_to_make_change = make_change(n, m, list_of_coins)
print(ways_to_make_change)
"""



# Test Case 1: expected answer: 4
# Test Case 2: expected answer: 5

in_str1 = ['4 3', '10 4']
in_str2 = ['1 2 3', '2 5 3 6']

for i in range(len(in_str1)):
	n, m = (int(x) for x in in_str1[i].strip().split(' '))
	list_of_coins = [int(x) for x in in_str2[i].strip().split(' ')]
	list_of_coins.sort()

	ways_to_make_change = make_change(n, m, list_of_coins)
	print(ways_to_make_change)
	print()


