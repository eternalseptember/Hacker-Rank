"""
This problem doesn't actually exist in hackerrank...
Think I might need this to form a base for another answer.
Not yet verified to pass all test cases in hackerrank.

Given a node to a tree, print the vertical order path
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


treeMap = []


def verticalOrder(node, level=0):
	if node is None:
		return None

	level -= 1
	if node.left is not None:
		verticalOrder(node.left, level)

	level += 1
	treeMap.append([level, node.data])

	if node.right is not None:
		level += 1
		verticalOrder(node.right, level)

	return treeMap


def verticalOrderPrint(treeMap):
	# get levels
	levels = []
	for i in treeMap:
		if i[0] not in levels:
			levels.append(i[0])

	levels.sort()
	treeLevels = []
	for i in levels:
		sameLevel = []
		for j in treeMap:
			if j[0] == i:
				sameLevel.append(j[1])
		treeLevels.append(sameLevel)

	for i in treeLevels:
		print(i)



# Binary tree setup
# test case 1: [4], [2], [1, 5, 6], [3], [7]
node4 = Node(4)
node5 = Node(5)
node2 = Node(2, node4, node5)
node6 = Node(6)
node7 = Node(7)
node3 = Node(3, node6, node7)
node1 = Node(1, node2, node3)

treeMap = verticalOrder(node1)
#for i in treeMap:
#	print(i)
#print()

verticalOrderPrint(treeMap)