"""
Input Format:
The first line contains an integer, t, denoting the number of trips
to the ice cream parlor. The 3t subsequent lines describe all of
Sunny and Johnny's trips to the parlor; each trip is described as
follows:
The first line contains m.
The second line contains n.
The third line contains n space-separated integers denoting the cost
of each respective flavor. The ith integer corresponding to the cost,
ci, for the ice cream with ID number i (where 1 <= i <= n).

Output Format:
Print two space-separated integers denoting the respective ID numbers
for the flavors they choose to purchase, where the smaller ID is printed
first and the larger ID is printed second. Recall that each ice cream
flavor has a unique ID number in the inclusive range from 1 to n.
"""


def find_flavors(m, n, arr):
	# Return the IDs (index start at 1) of the combination equalling m.
	flavors = []
	found = False

	for i in range(n - 1):
		if arr[i] >= m:
			continue
		else:
			for j in range(i + 1, n):
				if arr[j] >= m:
					continue
				else:
					if (arr[i] + arr[j] == m):
						flavors.extend([i + 1, j + 1])
						found = True
						break
		if found is False:
			continue
		else:
			break


	flavors.sort()
	return flavors


"""
t = int(input().strip())
for i in range(t):
	m = int(input().strip())
	n = int(input().strip())
	c = [int(temp) for temp in input().strip().split(' ')]
	flavors = find_flavors(m, n, c)
	print(*flavors, sep=' ')
"""


# test case 1, expected output:
# 1 4
# 1 2

t = 2  		# trips to parlor
m = [4, 4]  # pooled money
n = [5, 4]  # number of flavors
c = ['1 4 5 3 2', '2 2 4 3']  # cost per flavor

for i in range(t):
	m_i = m[i]
	n_i = n[i]
	cost = [int(temp) for temp in c[i].strip().split(' ')]
	flavors = find_flavors(m_i, n_i, cost)
	print(*flavors, sep=' ')


