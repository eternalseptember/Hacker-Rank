"""
This problem doesn't actually exist in hackerrank... yet...

Given a node to a tree, print the vertical order path
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


def verticalOrder(node):
	# stuff here




# Binary tree setup
# test case 1: [4], [2], [1, 5, 6], [3], [7]
node4 = Node(4)
node5 = Node(5)
node2 = Node(2, node4, node5)
node6 = Node(6)
node7 = Node(7)
node3 = Node(3, node6, node7)
node1 = Node(1, node2, node3)

verticalOrder(node1)
