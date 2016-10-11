"""
Get binary tree height, counting the edges.

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


def getHeight(root):
	if root is None:
		return -1

	left = getHeight(root.left)
	right = getHeight(root.right)

	return max(left, right) + 1


# setup
node7 = Node(7)
node6 = Node(6, None, node7)
node4 = Node(4)
node5 = Node(5, node4, node6)
node1 = Node(1)
node2 = Node(2, node1, None)
node3 = Node(3, node2, node5)

height = getHeight(node3)
print(height)
