"""
Definition:
The data value of every node in a node's left subtree
is less than the data value of that node.
The data value of every node in a node's right subtree
is greater than the data value of that node.

Given the root node of a binary tree, can you determine
if it's also a binary search tree?
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


def check_binary_search_tree(root):
	if root.left is not None:
		if root.left.data < root.data:
			check_binary_search_tree(root.left)
		else:
			return False

	if root.right is not None:
		if root.right.data > root.data:
			check_binary_search_tree(root.right)
		else:
			return False

	return True




node1 = Node(1)
node4 = Node(4)
node5 = Node(5, node1, node4)
node6 = Node(6)
node2 = Node(2, node6)
node3 = Node(3, node5, node2)

if check_binary_search_tree(node3):
	print("Yes")
else:
	print("No")
