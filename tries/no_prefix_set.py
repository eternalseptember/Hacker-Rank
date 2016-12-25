"""
Given N strings. Each string contains only lowercase letters from a-j
(both inclusive). The set of N strings is said to be GOOD SET if no
string is prefix of another string; else, it is BAD SET. (If two strings
are identical, they are considered prefixes of each other.)

For example, aab, abcde, aabcd is BAD SET because aab is prefix of aabcd.

Print GOOD SET if it satisfies the problem requirement.
Else, print BAD SET and the first string for which the condition fails.

Input Format:
First line contains N, the number of strings in the set.
Then next N lines follow, where i_th line contains i_th string.
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



def check_prefixes(list_of_strings):
	safe_strings = Trie_Node()

	for new_string in list_of_strings:
		try:
			if safe_strings.starts_with(new_string):
				return new_string
			if safe_strings.contains(new_string):
				return new_string

			# by this point, new string is a safe string
			safe_strings.insert(new_string)

		except KeyError:
			# the trie is empty, so insert string
			safe_strings.insert(new_string)

	# by this point, this is a good set
	return None


"""
N = int(input().strip())
strings = []

for i in range(N):
	str = input().strip()
	strings.append(str)

failed_string = check_prefixes(strings)

if failed_string is None:
	print('GOOD SET')
else:
	print('BAD SET')
	print(failed_string)
"""


"""
# Test case 1 expected result: BAD SET; aabcde
# Test case 2 expected result: BAD SET; aacghgh
N = [7, 4, 2, 2]
in_str1 = [['aab', 'defgab', 'abcde', 'aabcde', 'cedaaa', 'bbbbbbbbbb', 'jabjjjad'],
		   ['aab', 'aac', 'aacghgh', 'aabghgh'],
		   ['abc', 'abcde'],
		   ['abcde', 'abc']]


for i in range(len(N)):
	strings = []

	for j in range(N[i]):
		str = in_str1[i][j].strip()
		strings.append(str)

	failed_string = check_prefixes(strings)

	if failed_string is None:
		print('GOOD SET')
	else:
		print('BAD SET')
		print(failed_string)
	print()
"""



