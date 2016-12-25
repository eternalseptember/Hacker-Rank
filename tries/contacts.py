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


class Trie_Node(dict):
	__slots__ = ['count']

	def __init__(self):
		self.count = 0


	def __repr__(self):
		return str('End: {0}  Nodes: {1}'.format(self.complete_word, self.nodes.keys()))


	def insert(self, str):
		current = self

		for char in str:
			if char not in current:
				current[char] = Trie_Node()

			current.count += 1
			current = current[char]



	def find_partial(self, str):
		current = self

		for char in str:
			if char not in current:
				return 0

			current = current[char]

		return current.count


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


