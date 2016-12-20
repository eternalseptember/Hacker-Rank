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
	connected = []



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


