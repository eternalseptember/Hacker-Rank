"""
Note Single nodes should not be considered in the answer.

Input Format:
First line contains an integer N.
Each of the next N lines contain two space-separated integers, i_th
line contains G_i and B_i.

Output Format:
Print two space separated integers, the number of vertices in the
smallest and the largest components.
"""


def get_vertices(edges_list):
	smallest = 30000  # given in the constraints
	largest = 0

	list_of_sets = union_join(edges_list)

	for list in list_of_sets:
		size = len(list)
		if size > largest:
			largest = size
		if size < smallest:
			smallest = size

	return smallest, largest


def union_join(edges_list):
	list_of_sets = []

	for edge in edges_list:
		# create the first set
		if len(list_of_sets) == 0:
			first_set = set(edge)
			list_of_sets.append(first_set)
		else:
			# see if this edge can be added to any already-created set
			added = False
			for list in list_of_sets:
				if not list.isdisjoint(edge):
					list.update(edge)
					added = True
					break
			# if not, create a new set
			if added is False:
				new_set = set(edge)
				list_of_sets.append(new_set)

	if len(list_of_sets) == len(edges_list):
		return list_of_sets
	else:
		return union_join(list_of_sets)



"""
N = int(input().strip())
edges = []
for i in range(N):
	G, B = (int(temp) for temp in input().strip().split(' '))
	edges.append((G, B))

small, large = get_vertices(edges)
print('{0} {1}'.format(small, large))
"""


# Setting up test case 1
# Answer should be: 2 4
N = 5
in_str1 = ['1 6', '2 7', '3 8', '4 9', '2 6']
edges = []

for i in range(N):
	G, B = (int(temp) for temp in in_str1[i].strip().split())
	edges.append((G, B))

small, large = get_vertices(edges)
print('{0} {1}'.format(small, large))


