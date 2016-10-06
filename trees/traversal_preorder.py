"""
Complete the preOrder function in your editor below, which has
1 parameter: a pointer to the root of a binary tree.

It must print the values in the tree's preorder traversal as a
single line of space-separated values.
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


def preOrder(root):
	print(root.data, end=' ')
	if root.left is not None:
		preOrder(root.left)
	if root.right is not None:
		preOrder(root.right)


# Binary tree setup
node1 = Node(1)
node4 = Node(4)
node5 = Node(5, node1, node4)
node6 = Node(6)
node2 = Node(2, node6)
node3 = Node(3, node5, node2)

preOrder(node3)
