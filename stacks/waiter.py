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


from math import log


def stack_plates(stacked_plates, i):
	A_i = stacked_plates[:]  # stack for plates that were not divisible
	B_i = []  # stack for plates that were divisible with i-th prime
	B_final = []  # already sorted from top-to-bottom, in order

	generate_list_of_primes(i)

	for iter in range(1, i + 1):
		unsorted = A_i[:]
		A_i.clear()

		while (len(unsorted) > 0):
			plate = unsorted.pop()

			if divisible_by_prime(plate, iter):
				B_i.append(plate)
			else:
				A_i.append(plate)

		B_final += B_i[::-1]
		B_i.clear()

	return B_final + A_i[::-1]


def divisible_by_prime(plate_num, i):
	i_th_prime = list_of_primes[i - 1]
	if (plate_num % i_th_prime == 0):
		return True
	else:
		return False


list_of_primes = []
def generate_list_of_primes(num_of_primes):
	# Sieve of erasthanos
	if num_of_primes <= 2:
		list_of_primes.append(2)
		list_of_primes.append(3)
		return

	max_length = int(2 * num_of_primes * log(num_of_primes))
	sieve = [True] * max_length
	prime_num = 0

	for i in range(2, max_length):
		if sieve[i]:
			prime_num += 1
			list_of_primes.append(i)
			if prime_num == num_of_primes:
				return
			for j in range(2*i, max_length, i):
				# cross off all multiples of i
				sieve[j] = False




# N, Q = (int(temp) for temp in input().strip().split(' '))
# A0 = [int(temp) for temp in input().strip().split(' ')]

in_1 = '5 1'
in_2 = '3 4 7 6 5'

N, Q = (int(temp) for temp in in_1.strip().split(' '))
A0 = [int(temp) for temp in in_2.strip().split(' ')]

new_stack = stack_plates(A0, Q)
for i in new_stack:
	print(i)

# should be 4 6 3 7 5

