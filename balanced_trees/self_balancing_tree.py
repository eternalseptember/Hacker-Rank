"""
Output Format:
Insert the new value into the tree and return a pointer to
the root of the tree. Ensure that the tree remains balanced.

At the time of this commit, this problem was not available
for submission in python.
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None, height=0):
		self.data = data
		self.left = left_node
		self.right = right_node
		self.height = height

	def __str__(self):
		return str(self.data)


def insert(root, value):
	root = insert_node(root, value)
	return root


def insert_node(root, value):
	if root is None:
		return Node(value)

	if value < root.data:
		if root.left is None:
			root.left = Node(value)
		else:
			insert_node(root.left, value)
	elif root.data < value:
		if root.right is None:
			root.right = Node(value)
		else:
			insert_node(root.right, value)

	return root


def get_balance_factor(node, value):
	balanceFactor = get_height(node.left) - get_height(node.right)
	# print(balanceFactor)
	return balanceFactor


def get_height(root):
	if root is None:
		return -1

	left = get_height(root.left)
	right = get_height(root.right)

	return max(left, right) + 1


def print_in_order(root):
	if root.left is not None:
		print_in_order(root.left)
	# print(root.data, end=' ')
	print('node: {0}  left: {1}  right: {2}'.format(root.data, root.left, root.right))
	if root.right is not None:
		print_in_order(root.right)



# BST setup
node5 = Node(5, None, None, 0)
node4 = Node(4, None, node5, 1)
node2 = Node(2, None, None, 0)
node3 = Node(3, node2, node4, 2)

root = insert(node3, 6)
print_in_order(root)
# answer should be 2 3 4 5 6
