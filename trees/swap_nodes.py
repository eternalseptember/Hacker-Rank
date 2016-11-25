"""
You are given a tree of N nodes where nodes are indexed from
[1..N] and it is rooted at 1. You have to perform T swap
operations on it, and after each swap operation print the
inorder traversal of the current state of the tree.

Input Format:
First line of input contains N, number of nodes in tree. Then
N lines follow. Here each of ith line (1 <= i <= N) contains
two integers, a b, where a is the index of left child, and b
is the index of right child of ith node. -1 is used to represent
null node.

Next line contain an integer, T. Then again T lines follows. Each
of these line contains an integer K.

Output Format:
For each K, perform swap operation as mentioned above and print
the inorder traversal of the current state of tree.
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None, depth=None):
		self.data = data
		self.left = left_node
		self.right = right_node
		self.depth = depth

	def __str__(self):
		return str(self.data)


queue = []
def insert(root, value, left=None, right=None):
	if (left == -1) and (right == -1) and (root is not None):
		# this node was already created
		return root

	left_node = None
	right_node = None

	if root is None:
		if left > 0:
			left_node = Node(left, depth=2)
		if right > 0:
			right_node = Node(right, depth=2)

		return Node(value, left_node, right_node, 1)

	else:
		if root.data == value:
			if left > 0:
				left_node = Node(left, depth=root.depth + 1)
			if right > 0:
				right_node = Node(right, depth=root.depth + 1)

			root.left = left_node
			root.right = right_node

			queue.clear()
		else:
			if root.left is not None:
				queue.append(root.left)
			if root.right is not None:
				queue.append(root.right)

			next_node = queue.pop(0)
			insert(next_node, value, left, right)

		return root


def print_in_order(root):
	if root.left is not None:
		print_in_order(root.left)
	print(root.data, end=' ')
	# print('{0}({1})'.format(root.data, root.depth), end=' ')
	if root.right is not None:
		print_in_order(root.right)


def in_order_queue(root):
	if root.left is not None:
		in_order_queue(root.left)
	queue.append(root)
	if root.right is not None:
		in_order_queue(root.right)


def swapping_nodes(root, k):
	in_order_queue(root)
	swap(k)

	print_in_order(root)
	print()


def swap(k):
	while len(queue) > 0:
		node = queue.pop(0)
		if (node.depth % k == 0):
			node.left, node.right = node.right, node.left
	


"""
n = int(input().strip())
root = None

for i in range(n):
	left, right = (int(temp) for temp in input().split(' '))
	root = insert(root, i + 1, left, right)

t = int(input().strip())
for i in range(t):
	k = int(input().strip())
	swapping_nodes(root, k)
"""


# setting up test case 1
# expected answer:
# 3 1 2
# 2 1 3

n = 3
in_str_1 = ['2 3', '-1 -1', '-1 -1']
root = None

for i in range(n):
	left, right = (int(temp) for temp in in_str_1[i].split(' '))
	root = insert(root, i + 1, left, right)

t = 2
in_str_2 = ['1', '1']

for i in range(t):
	k = int(in_str_2[i].strip())
	swapping_nodes(root, k)




# setting up test case 2
# expected answer:
# 4 2 1 5 3

n = 5
in_str_1 = ['2 3', '-1 4', '-1 5', '-1 -1', '-1 -1']
root = None

for i in range(n):
	left, right = (int(temp) for temp in in_str_1[i].split(' '))
	root = insert(root, i + 1, left, right)

t = 1
in_str_2 = ['2']

for i in range(t):
	k = int(in_str_2[i].strip())
	swapping_nodes(root, k)




# setting up test case 3
# expected answer:
# 2 9 6 4 1 3 7 5 11 8 10
# 2 6 9 4 1 3 7 5 10 8 11

n = 11
in_str_1 = ['2 3', '4 -1', '5 -1', '6 -1', '7 8', '-1 9', '-1 -1', '10 11', '-1 -1', '-1 -1', '-1 -1']
root = None

for i in range(n):
	left, right = (int(temp) for temp in in_str_1[i].split(' '))
	root = insert(root, i + 1, left, right)

t = 2
in_str_2 = ['2', '4']

for i in range(t):
	k = int(in_str_2[i].strip())
	swapping_nodes(root, k)


