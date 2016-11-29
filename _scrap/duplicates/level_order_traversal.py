"""
Input Format:
The locked stub code in your editor reads the following inputs
and assembles them into a BST:
The first line contains an integer, T (the number of test cases).
The T subsequent lines each contain an integer, data, denoting
the value of an element that must be added to the BST.

Output Format:
Print the data value of each node in the tree's level-order
traversal as a single line of N space-separated integers.
"""




class Node:
	def __init__(self, data):
		self.right = self.left = None
		self.data = data


class Solution:
	def insert(self, root, data):
		if root is None:
			return Node(data)
		else:
			if data <= root.data:
				cur = self.insert(root.left, data)
				root.left = cur
			else:
				cur = self.insert(root.right, data)
				root.right = cur
		return root


	queue = []

	def levelOrder(self, root):
		if root.left is not None:
			self.queue.append(root.left)
		if root.right is not None:
			self.queue.append(root.right)

		print(root.data, end=' ')

		if len(self.queue) > 0:
			nextNode = self.queue.pop(0)
			self.levelOrder(nextNode)




T = 6
data_in = [3, 5, 4, 7, 2, 1]

# T = int(input())
myTree = Solution()
root = None
for i in range(T):
	# data = int(input())
	data = data_in[i]
	root = myTree.insert(root, data)
myTree.levelOrder(root)
