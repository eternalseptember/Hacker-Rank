"""
In the event that this problem allows python submissions in the future,
reformatting this answer to be consistent with the other problems in
this folder.
"""


class Node(object):
	def __init__(self, data=None, left_node=None, right_node=None):
		self.data = data
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


queue = []
def levelOrder(root):
	if root.left is not None:
		queue.append(root.left)
	if root.right is not None:
		queue.append(root.right)

	print(root.data, end=' ')

	if len(queue) > 0:
		queue.reverse()
		nextNode = queue.pop()
		queue.reverse()
		levelOrder(nextNode)



# Binary tree setup
node4 = Node(4)
node7 = Node(7)
node5 = Node(5, node4, node7)
node1 = Node(1)
node2 = Node(2, node1, None)
node3 = Node(3, node2, node5)

levelOrder(node3)
