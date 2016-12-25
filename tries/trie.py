"""
Trying to implement a trie.
"""


class Trie_Node:
	def __init__(self, terminal=False):
		# dictionary to store { character: Trie_Node }
		self.nodes = {}
		self.terminal = terminal


	def insert_char(self, char):
		self.nodes[char] = True_Node(False)
		return self.nodes[char]


	def insert_str(self, str):
		trie = None

		for char in str:
			trie = self.search(char)
			if trie is not False:
				continue
			else:
				trie = self.insert_char(char)

		# by this point, insert a terminal
		


	def search(self, char):
		if char in self.node:
			return self.node[char]
		else:
			return False


	def startsWith(self, prefix):
		# stuff here




