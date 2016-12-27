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


