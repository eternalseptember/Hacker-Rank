"""
You are given a pointer to the root of a binary search tree and a value
to be inserted into the tree. Insert this value into its appropriate
position in the binary search tree and return the root of the updated
binary tree.

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


def insert(root, value):
	new_node = Node(value)
	print(new_node)






# Binary Tree Setup
node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)
node7 = Node(7)
node4 = Node(4, node2, node7)

insert(node4, 6)

