"""
Input Format:
The locked stub code in your editor reads the following inputs
and assembles them into a binary search tree: The first line
contains an integer, n, denoting the number of nodes in the
tree. Each of the n subsequent lines contains an integer, data,
denoting the value of an element that must be added to the BST.

Output Format:
The locked stub code in your editor will print the integer
returned by your getHeight function denoting the height of
the BST.
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


# Solution here
	def getHeight(self, root):
		if root is None:
			return -1

		left = self.getHeight(root.left)
		right = self.getHeight(root.right)

		return max(left, right) + 1



# More stub code
T = 7
data_in = [3, 5, 2, 1, 4, 6, 7]

# T = int(input())
myTree = Solution()
root = None

for i in range(T):
	# data = int(input())
	data = data_in[i]
	root = myTree.insert(root, data)

height = myTree.getHeight(root)

print(height)
