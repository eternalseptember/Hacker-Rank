"""
Suppose there is a circle. There are N petrol pumps on that
circle. Petrol pumps are numbered 0 to (N-1) (both inclusive).

Initially, you have a tank of infinite capacity carrying no
petrol. You can start the tour at any of the petrol pumps.
Calculate the first point from where the truck will be able
to complete the circle. Consider that the truck will stop at
each of the petrol pumps. The truck will move one kilometer
for each litre of the petrol.

Input Format:
The first line will contain the value of N.
The next N lines will contain a pair of integers each, i.e.
the amount of petrol that petrol pump will give and the
distance between that petrol pump and the next petrol pump.

Output Format:
An integer which will be the smallest index of the petrol
pump from which we can start the tour.
"""


def calc_fuel(amt, dist):
	# do math here



# n = int(input().strip())
station = None

# setting up test case 1
n = 3
in_str1 = ['1 5', '10 3', '3 4']

for i in range(n):
	# amt, dist = (int(temp) for temp in input().strip().split(' '))
	amt, dist = (int(temp) for temp in in_str1[i].strip().split(' '))

	result = calc_fuel
	# set the station number to i

print(station)
# expected result: 1
