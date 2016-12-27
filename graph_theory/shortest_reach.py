"""
Consider an undirected graph consisting of n nodes where each node is
labeled from 1 to n and the edge between any two nodes is always of
length 6. We define node s to be the starting position for a BFS.

Given q queries in the form of a graph and some starting node, s,
perform each query by calculating the shortest distance from starting
node s to all the other nodes in the graph. Then print a single line
of n-1 space-separated integers listing node s's shortest distance to
each of the n-1 other nodes (ordered sequentially by node number); if
s is disconnected from a node, print -1 as the distance to that node.
"""


def calc_distance(n, s, edges_list):
	# populate adjancency list
	nodes = {}
	for edge in edges_list:
		u, v = (edge)

		if u not in nodes:
			nodes[u] = []
		nodes[u].append(v)

		if v not in nodes:
			nodes[v] = []
		nodes[v].append(u)

	print(nodes)

	# node = i + 1
	dist = [0 for i in range(n)]
	for i in range(n):
		if s == i + 1:
			# starting node
			continue

		if (i + 1) not in nodes:
			# node has no edges
			dist[i] = -1
			continue

		if (i + 1) in nodes[s]:
			# if there's a direct connection
			# edge between any two nodes is 6
			dist[i] = 6



	# delete starting node
	del dist[s-1]

	return dist




# setting up test case 1. expected answer:
# 6 6 -1
# -1 6

# Number of queries
# q = int(input().strip())
q = 2
in_str1 = ['4 2', '1 2', '1 3', '1', '3 1', '2 3', '2']


for i in range(q):
	# n: number of nodes;  m: number of edges
	# n, m = (int(temp) for temp in input().strip().split(' '))
	inp = in_str1.pop(0)
	n, m = (int(temp) for temp in inp.strip().split(' '))


	edges_list = []
	for j in range(m):
		# edge connecing node u to node v
		# u, v = (int(temp) for temp in input().strip().split(' '))
		inp = in_str1.pop(0)
		u, v = (int(temp) for temp in inp.strip().split(' '))
		edges_list.append((u, v))


	# Starting node
	# s = int(input().strip())
	inp = in_str1.pop(0)
	s = int(inp.strip())

	dist_list = calc_distance(n, s, edges_list)
	print(*dist_list, sep=' ')


