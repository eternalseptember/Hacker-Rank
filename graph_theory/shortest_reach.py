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
	graph = {}
	for edge in edges_list:
		u, v = (edge)

		if u not in graph:
			graph[u] = []
		if v not in graph[u]:
			graph[u].append(v)

		if v not in graph:
			graph[v] = []
		if u not in graph[v]:
			graph[v].append(u)

	# Dijkstra's algorithm
	map_heap = {}  # keeps track of minimum
	dist_map = {}  # shortest distance from source node
	path_map = {}  # key: node; value: node's parent

	# initialize the map heap
	for i in range(1, n+1):
		map_heap[i] = None

	# source node's distance is zero
	map_heap[s] = 0
	path_map[s] = None
	dist_length = 6  # weighted graph, but all edges are weighed equally

	while len(map_heap) > 0:
		# At the beginning of every iteration, find the min value.
		# If min value is not None, then store it in dist_map and
		# then remove it from map_heap.
		min_index = get_min(map_heap)

		#print('min_index: {0}'.format(min_index))

	# If min value is none, then the node is not connected to the source.
		if min_index is None:
			break

		dist_map[min_index] = map_heap[min_index]
		del map_heap[min_index]

		try:
			# find the distance to source for every node connected to min_index
			connections = graph[min_index]
		except KeyError:
			# the source node has no connections
			break

		#print('connections: ', end=' ')
		#print(connections)

		for node in connections:
			#print('node: {0}'.format(node))

			if node in dist_map:
				continue
			else:
				if map_heap[node] is None:
					if min_index == s:
						map_heap[node] = dist_length
					else:
						# traverse the known nodes, then multiply for total distance
						print('\tNo distance recorded yet, so trying to find path to source.')
						print('\tsource: {0}  min_index: {1}  node: {2}'.format(s, min_index, node))
						path = find_shortest_path_to_source(s, min_index, path_map)
						map_heap[node] = len(path) * dist_length

					path_map[node] = min_index

				else:
					# check if the new distance is lower than the distance in map_heap
					path = find_shortest_path_to_source(s, node, path_map)
					new_dist = len(path) * dist_length

					if new_dist < map_heap[node]:
						map_heap[node] = new_dist
						path_map[node] = min_index  # update the parent node

	# format the answer
	dist = [0 for i in range(n)]
	for i in range(n):
		# node = i + 1
		if (i + 1) in dist_map:
			dist[i] = dist_map[i + 1]
		else:
			dist[i] = -1

	# delete starting node
	del dist[s-1]

	return dist



def get_min(map_heap):
	# Output the key corresponding to the lowest value
	# In the event of a tie, returns the first set found
	lowest = None
	lowest_key = None

	for key in map_heap.keys():
		if map_heap[key] is None:
			continue
		else:
			if (lowest is None) or (map_heap[key] < lowest):
				lowest = map_heap[key]
				lowest_key = key

	return lowest_key


def find_shortest_path_to_source(source_node, final_node, path_map):
	current_node = final_node
	source_found = False
	path = [current_node]

	while source_found is False:
		parent_node = path_map[current_node]
		path.append(parent_node)

		if parent_node == source_node:
			source_found = True
		else:
			current_node = parent_node

	return path



# setting up test case 1. expected answer:
# 6 6 -1
# -1 6

"""
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
"""

