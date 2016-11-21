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
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


def inOrder(root):
	if root.left is not None:
		inOrder(root.left)
	print(root.data, end=' ')
	if root.right is not None:
		inOrder(root.right)


def swapping_nodes(k):
	# stuff here
	print(k)


"""
n = int(input().strip())
for i in range(n):
	left, right = (int(temp) for temp in input().split(' '))

t = int(input().strip())
for i in range(t):
	k = int(input().strip())
	swapping_nodes(k)
"""


# setting up test case 1
# expected answer:
# 3 1 2
# 2 1 3

n = 3
in_str_1 = ['2 3', '-1 -1', '-1 -1']

for i in range(n):
	left, right = (int(temp) for temp in in_str_1[i].split(' '))
	# print(left, right)


t = 2
in_str_2 = ['1', '1']

for i in range(t):
	k = int(in_str_2[i].strip())
	swapping_nodes(k)


