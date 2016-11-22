"""
Huffman coding assigns variable length codewords to fixed
length input characters based on their frequencies. A Huffman
tree is made for the input string and characters are decoded
based on their position in the tree. We add a '0' to the
codeword when we move left in the binary tree and a '1' when
we move right in the binary tree.

You are given pointer to the root of the Huffman tree and a
binary coded string. You need to print the actual string.

At the time of this commit, this problem was not available
for submission in python.
"""


class Node(object):
	# Node was modified for this problem
	def __init__(self, data=None, freq=None, left_node=None, right_node=None):
		self.data = data
		self.freq = freq
		self.left = left_node
		self.right = right_node

	def __str__(self):
		return str(self.data)


def decode_huff(node, str):
	# stuff here
	print(node)




# Tree setup
nodeB = Node('B', 1)
nodeC = Node('C', 1)
node1 = Node(None, 2, nodeB, nodeC)
nodeA = Node('A', 3)
node2 = Node(None, 5, node1, nodeA)

s = '1001011'

# expected output: ABACA
decode_huff(node2, s)
