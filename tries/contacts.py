"""
Input Format:
The first line contains a single integer, n, denoting the number of operations
to perform.
Each line i of the n subsequent lines contains an operation in one of the two
forms defined above.

Output Format:
For each find partial operation, print the number of contact names starting
with partial on a new line.
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


	def find_partial(self, str):
		current = self

		for char in str:
			if char not in current.nodes:
				return 0

			current = current.nodes[char]

		# at this point, traverse the rest of the trie
		return self.count_branches(current)


	def count_branches(self, current):
		count = 0

		if current.complete_word:
			count += 1

		keys = current.nodes.keys()
		for key in keys:
			count += self.count_branches(current.nodes[key])

		return count


# n = int(input().strip())
n = 4
in_str1 = ['add hack', 'add hackerrank', 'find hac', 'find hak']


contacts = Trie_Node()
for i in range(n):
	# opp, name = input().strip().split()
	opp, name = in_str1[i].strip().split()

	if opp == 'add':
		contacts.insert(name)
	else:
		matches = contacts.find_partial(name)
		print(matches)


