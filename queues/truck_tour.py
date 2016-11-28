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


def calc_fuel(possible_start, station_list):
	total_fuel = 0

	for station_num in possible_start:
		# build a circular station list
		init1 = station_list[:station_num]
		init2 = station_list[station_num:]
		new_station_list = init2 + init1

		# cycle through the new station list
		for station in new_station_list:
			amt = station[0]
			dist = station[1]

			total_fuel += (amt - dist)

			if total_fuel < 0:
				# this is not a correct starting station
				break

		if total_fuel < 0:
			# continue to next possible starting station
			continue
		else:
			return station_num



# n = int(input().strip())
station_list = []    # tuples of (amt, dist)
possible_start = []  # index of station_list

# setting up test case 1
n = 3
in_str1 = ['1 5', '10 3', '3 4']


for i in range(n):
	# amt, dist = (int(temp) for temp in input().strip().split(' '))
	amt, dist = (int(temp) for temp in in_str1[i].strip().split(' '))
	station_list.append((amt, dist))

	if amt >= dist:
		possible_start.append(i)


station = calc_fuel(possible_start, station_list)
print(station)
# expected result: 1
