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

	def __init__(self, count=0, is_leaf=False):
		self.count = count
		self.is_leaf = is_leaf  # Word end


	def __repr__(self):
		return str('Count: {0}  Leaf: {1}  Nodes: {2}'.
					format(self.count, self.is_leaf, self.keys()))


def insert(head, str):
	current = head
	current.count += 1  # Placed here for recursive calls

	for key in current.keys():
		prefix, post_key, post_str = get_prefix(key, str)

		if post_key == '':
			# the key in the dictionary is a prefix for the str

		if prefix != '':
			# if there is a prefix, split
			# add node with key's suffix, post_key
			# add node with string's suffix, post_str

	# Gets to this point if there are no keys or all the keys have been iterated
	current[str] = Trie_Node(1, True)

	return head


def find_partial(head, str):
	current = head

	for char in str:
		if char not in current:
			return 0

		current = current[char]

	return current.count


def get_prefix(str1, str2):
	cut = 0
	for char1, char2 in zip(str1, str2):
		if char1 != char2:
			break
		cut += 1
	return str1[:cut], str1[cut:], str2[cut:]




# n = int(input().strip())
n = [4, 11]
in_str1 = [['add hack', 'add hackerrank', 'find hac', 'find hak'], 
		   ['add s', 'add ss', 'add sss', 'add ssss', 'add sssss', 'find s',
		    'find ss', 'find sss', 'find ssss', 'find sssss', 'find ssssss']]

for i in range(len(n)):
	head = Trie_Node()

	for j in range(n[i]):
		# opp, name = input().strip().split()
		opp, name = in_str1[i][j].strip().split()

		if opp == 'add':
			head = insert(head, name)
		else:
			matches = find_partial(head, name)
			print(matches)

	print()



