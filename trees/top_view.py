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
	leftView(node.left)
	print(node.data, end=' ')
	rightView(node.right)


def leftView(node):
	if node is None:
		return
	leftView(node.left)
	print(node.data, end=' ')


def rightView(node):
	if node is None:
		return
	print(node.data, end=' ')
	rightView(node.right)




# Binary Tree Setup
# test case 1: 1 5 3 2 7
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


"""
# The following test cases came from other sources, not
# guaranteed to be following hackerrank's definitions.

# test case 2: 2 1 3 6
node6 = Node(6)
node5 = Node(5, None, node6)
node4 = Node(4, None, node5)
node2 = Node(2, None, node4)
node3 = Node(3)
node1 = Node(1, node2, node3)

topView(node1)

# test case 3: 8 4 2 1 3 7
node8 = Node(8)
node9 = Node(9)
node4 = Node(4, node8, node9)
node5 = Node(5)
node2 = Node(2, node4, node5)
node6 = Node(6)
node7 = Node(7)
node3 = Node(3, node6, node7)
node1 = Node(1, node2, node3)

topView(node1)
"""