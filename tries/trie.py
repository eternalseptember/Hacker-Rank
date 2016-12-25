"""
Trying to implement a trie.
"""


class Trie_Node:
	def __init__(self, complete_word=False):
		# dictionary to store { character: Trie_Node }
		self.nodes = {}
		self.complete_word = complete_word


	def __repr__(self):
		return str('End: {0}  Nodes: {1}'.format(self.complete_word, self.nodes.keys()))


	def insert(self, str):
		current = self

		for char in str:
			if char not in current.nodes:
				current.nodes[char] = Trie_Node()

			current = current.nodes[char]

		current.complete_word = True


	def search(self, str):
		current = self

		for char in str:
			if char not in current.nodes:
				return False

			current = current.nodes[char]

		return current.complete_word


	def starts_with(self, str):
		# Does the trie contain str?
		current = self

		for char in str:
			if char not in current.nodes:
				return False

			current = current.nodes[char]

		return True


	def contains(self, str):
		# Does the str contain a stored prefix?
		current = self

		for char in str:
			if current.complete_word:
				return True

			current = current.nodes[char]

		return current.complete_word


# Testing
# scenario 1: ['abcde', 'abc']
test = Trie_Node()
word1 = 'birds'
word2 = 'bird'

test.insert(word1)
res = test.starts_with(word2)
print('New string \'{0}\' is in a stored prefix \'{1}\'. {2}'.format(word2, word1, res))
res = test.contains(word2)
print('New string \'{0}\' contains stored prefix \'{1}\'. {2}'.format(word2, word1, res))
print()


# scenario 2: ['abc', 'abcde']
test = Trie_Node()
word1 = 'bird'
word2 = 'birds'

test.insert(word1)
res = test.starts_with(word2)
print('New string \'{0}\' is in a stored prefix \'{1}\'. {2}'.format(word2, word1, res))
res = test.contains(word2)
print('New string \'{0}\' contains stored prefix \'{1}\'. {2}'.format(word2, word1, res))

