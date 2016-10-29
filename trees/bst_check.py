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


def check_binary_search_tree_(root, min=0, max=10000):
	if root is None:
		return True

	#print("min: {0}, root:{1}, max: {2}".format(min, root, max))
	if ((root.data > min) and
		(root.data < max) and
		(check_binary_search_tree_(root.left, min, root.data)) and
		(check_binary_search_tree_(root.right, root.data, max))):
		return True
	else:
		return False
	



# test case 1: no
node1 = Node(1)
node4 = Node(4)
node5 = Node(5, node1, node4)
node6 = Node(6)
node2 = Node(2, node6)
node3 = Node(3, node5, node2)

if check_binary_search_tree_(node3):
	print("Yes")
else:
	print("No")
print()

# test case 2: no
node2 = Node(2)
node6 = Node(6)
node7 = Node(7)
node9 = Node(9)
node3 = Node(3, node2, node6)
node8 = Node(8, node7, node9)
node5 = Node(5, node3, node8)

if check_binary_search_tree_(node5):
	print("Yes")
else:
	print("No")
print()

# test case 3: yes
node1 = Node(1)
node4 = Node(4)
node3 = Node(3, node1, node4)
node6 = Node(6)
node5 = Node(5, node3, node6)
node8 = Node(8)
node10 = Node(10)
node9 = Node(9, node8, node10)
node13 = Node(13)
node17 = Node(17)
node15 = Node(15, node13, node17)
node12 = Node(12, node9, node15)
node7 = Node(7, node5, node12)

if check_binary_search_tree_(node7):
	print("Yes")
else:
	print("No")
print()
