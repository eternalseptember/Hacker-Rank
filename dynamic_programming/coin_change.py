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


def make_change(total, list_of_coins):
	# base cases
	if total <= 0:
		return 0
	elif len(list_of_coins) == 0:
		return 0
	elif len(list_of_coins) == 1:
		if total % list_of_coins[0] == 0:
			return 1
		else:
			return 0

	total_ways = 0
	first_coin = list_of_coins.pop()
	first_coin_max = total // first_coin

	for first_coin_amt in range(0, first_coin_max + 1):
		remaining = total - (first_coin * first_coin_amt)
		total_ways += make_change(remaining, list_of_coins)

	return total_ways






"""
n, m = (int(x) for x in input().strip().split(' '))
list_of_coins = [int(x) for x in input().strip().split(' ')]
list_of_coins.sort()
ways_to_make_change = make_change(n, list_of_coins)
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

	print('total amount: {0},  coins:'.format(n), end=' ')
	print(list_of_coins)
	ways_to_make_change = make_change(n, list_of_coins)
	print(ways_to_make_change)



