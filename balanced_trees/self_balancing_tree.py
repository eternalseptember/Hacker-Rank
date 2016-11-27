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
	update_heights(root)
	root = balance(root)
	return root


def insert_node(root, value):
	if root is None:
		return Node(value)

	if value < root.data:
		root.left = insert_node(root.left, value)
	elif root.data < value:
		root.right = insert_node(root.right, value)

	return root


def get_balance_factor(root):
	return get_height(root.left) - get_height(root.right)


def update_heights(root):
	queue.clear()
	in_order_queue(root)
	while len(queue) > 0:
		node = queue.pop()
		node.height = get_height(node)


def get_height(root):
	if root is None:
		return -1

	left = get_height(root.left)
	right = get_height(root.right)

	return max(left, right) + 1


def balance(root):
	if root is None:
		return root

	# change pointers to new roots here
	balance_factor = get_balance_factor(root)

	if balance_factor > 1:
		balance_factor_L = get_balance_factor(root.left)

		if balance_factor_L == -1:
			root = rotateLR(root)
		# elif (balance_factor_L == 1) or (balance_factor_L == 0):
		elif (balance_factor_L == 1):
			root = rotateLL(root)
		else:
			root.left = balance(root.left)

		root = balance(root)

	elif balance_factor < -1:
		balance_factor_R = get_balance_factor(root.right)

		if balance_factor_R == 1:
			root = rotateRL(root)
		# elif (balance_factor_R == -1) or (balance_factor_R == 0):
		elif (balance_factor_R == -1):
			root = rotateRR(root)
		else:
			root.right = balance(root.right)

		root = balance(root)

	else:
		root.left = balance(root.left)
		root.right = balance(root.right)

	update_heights(root)
	return root


def rotateLL(root):
	# unbalanced when a node is inserted into the
	# left subtree of root's left subtree

	old_root = root
	new_root = old_root.left
	old_root.left = new_root.right
	new_root.right = old_root
	update_heights(new_root)

	return new_root


def rotateRR(root):
	# unbalanced when a node is inserted into the
	# right subtree of root's right subtree

	old_root = root
	new_root = old_root.right
	old_root.right = new_root.left
	new_root.left = old_root
	update_heights(new_root)

	return new_root


def rotateLR(root):
	# unbalanced when a node is inserted into the
	# right subtree of the root's left subtree

	# root is node1, node1's left is node2, node2's right is node3
	node2 = root.left
	node3 = node2.right
	node2.right = node3.left
	root.left = node3
	node3.left = node2
	new_root = rotateLL(root)

	return new_root


def rotateRL(root):
	# unbalanced when a node is inserted into the
	# left subtree of the root's right subtree

	# root is node1, node1's right is node2, node2's left is node3
	node2 = root.right
	node3 = node2.left
	node2.left = node3.right
	root.right = node3
	node3.right = node2
	new_root = rotateRR(root)

	return new_root


queue = []
def in_order_queue(root):
	if root.left is not None:
		in_order_queue(root.left)
	queue.append(root)
	if root.right is not None:
		in_order_queue(root.right)


# Helper print functions to help with debugging
def print_in_order(root):
	if root.left is not None:
		print_in_order(root.left)
	# print('node: {0}  left: {1}  right: {2}  height: {3}'.format(root.data, root.left, root.right, root.height))
	print('{0}({1})'.format(root.data, get_balance_factor(root)), end=' ')
	if root.right is not None:
		print_in_order(root.right)


"""
# Test case 0
node5 = Node(5, None, None, 0)
node4 = Node(4, None, node5, 1)
node2 = Node(2, None, None, 0)
node3 = Node(3, node2, node4, 2)

root = insert(node3, 6)
print_in_order(root)
print('\n')
# answer should be...
# 2(0) 3(-1) 4(0) 5(0) 6(0)
"""


# Test case 1
root = None
in_str = [14, 25, 21, 10, 23, 7, 26, 12, 30, 16, 19]
for i in in_str:
	print('Inserting {0}:  '.format(i), end=' ')
	root = insert(root, i)
	print_in_order(root)
	print()

# answer should be...
# 7(0) 10(0) 12(0) 14(0) 16(-1) 19(0) 21(0) 23(0) 25(-1) 26(-1) 30(0)

