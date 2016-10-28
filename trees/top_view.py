"""
You are given a pointer to the root of a binary tree.
Print the top view of the binary tree.

At the time of this commit, this problem was not available
for submission in python.
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


def topView(node):
	# stuff here





# Binary Tree Setup
node9 = Node(9)
node1 = Node(1, None, node9)
node4 = Node(4)
node5 = Node(5, node1, node4)
node8 = Node(8)
node7 = Node(7, node8, None)
node6 = Node(6)
node2 = Node(2, node6, node7)
node3 = Node(3, node5, node2)

topView(node3)
