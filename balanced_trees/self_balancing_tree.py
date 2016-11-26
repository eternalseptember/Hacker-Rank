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
	update_height(root)
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


def update_height(root):
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
		# balance left subtree
	elif balance_factor < -1:
		# balance right subtree
	else:
		root.left = balance(root.left)
		root.right = balance(root.right)

	return root 


def rotateLL(root):
	# unbalanced when a node is inserted into the
	# left subtree of root's left subtree

	# break root's left connection first
	old_root = root
	new_root = old_root.left
	old_root.left = None
	# then reassign and update height
	new_root.right = old_root
	update_height(new_root)

	return new_root


def rotateRR(root):
	# unbalanced when a node is inserted into the
	# right subtree of root's right subtree

	# break root's right connection first
	old_root = root
	new_root = old_root.right
	old_root.right = None
	# then reassign and update height
	new_root.left = old_root
	update_height(new_root)

	return new_root


def rotateLR(root):
	# unbalanced when a node is inserted into the
	# right subtree of the root's left subtree

	# nodeC is root, nodeC's left is nodeA, and nodeA's right is nodeB
	nodeA = root.left
	nodeB = nodeA.right
	# break nodeA's connection to nodeB
	nodeA.right = None
	# reassign
	root.left = nodeB
	nodeB.left = nodeA
	new_root = rotateLL(root)

	return new_root


def rotateRL(root):
	# unbalanced when a node is inserted into the
	# left subtree of the root's right subtree

	# nodeA is root, nodeA's right is nodeC, nodeC's left is nodeB
	nodeC = root.right
	nodeB = nodeC.left
	# break nodeC's connection to nodeB
	nodeC.left = None
	# reassign
	root.right = nodeB
	nodeB.right = nodeC
	new_root = rotateRR(root)

	return new_root


queue = []
def in_order_queue(root):
	if root.left is not None:
		in_order_queue(root.left)
	queue.append(root)
	if root.right is not None:
		in_order_queue(root.right)


def print_in_order(root):
	if root.left is not None:
		print_in_order(root.left)
	# print(root.data, end=' ')
	print('node: {0}  left: {1}  right: {2}  height: {3}'.format(root.data, root.left, root.right, root.height))
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
