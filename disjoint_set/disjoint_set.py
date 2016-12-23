"""
An attempt to implement a disjoint set to be used for problems in this section.
"""


from collections import Counter


class Element:
	def __init__(self, parent=None):
		self.parent = parent
		self.rank = 0

	def __str__(self):
		return str(self.parent)


class Disjoint_Set:
	def __init__(self):
		self.sets = []


	def get_results(self):
		# Get the final printed results from this function
		counts = self.get_counts()

		# Smallest set
		small_list = counts.most_common()[::-1]
		for item in small_list:
			small_par, count = (item)
			if count == 1:
				continue
			else:
				break
		
		# Largest set
		lar_par, large = (counts.most_common(1)[0])

		return str(count) + ' ' + str(large)


	def get_counts(self):
		# The final count might not be fully right due to path compression.
		for i in range(len(self.sets)):
			self.find_parent(i)

		# Tally
		freq = []
		for item in self.sets:
			freq.append(item.parent)
		counts = Counter(freq)
		return counts


	def nodes_in_set(self):
		# A helper function for troubleshooting only
		items = ''
		for i in range(len(self.sets)):
			items += 'Node ' + str(i+1) + ': Parent: ' + str(self.sets[i].parent) + ' Rank: ' + str(self.sets[i].rank) + '\n'
		return items


	def make_set(self, N):
		# Assumes the set was empty when this function is called.
		# Make 2N nodes, and store it in self.sets
		for i in range(1, 2*N+1):
			new_item = Element(i)
			self.sets.append(new_item)

		"""
		for item in self.sets:
			print(str(item), end=' ')
		"""


	def union(self, num1, num2):
		# Array is 0-based, but N begins at 1
		item1 = self.sets[num1-1]
		item2 = self.sets[num2-1]

		#print('Pre union: what is in these specific locations?')
		#print('Parent: {0}  Rank: {1}'.format(item1, item1.rank))
		#print('Parent: {0}  Rank: {1}'.format(item2, item2.rank))

		item1_parent = self.find_parent(item1.parent)
		item2_parent = self.find_parent(item2.parent)
		item1_parent_rank = self.sets[item1_parent-1].rank
		item2_parent_rank = self.sets[item2_parent-1].rank

		#print('What are each item\'s roots?')
		#print('Parent: {0}  Rank: {1}'.format(item1_parent, item1_parent_rank))
		#print('Parent: {0}  Rank: {1}'.format(item2_parent, item2_parent_rank))

		if item1_parent_rank == item2_parent_rank:
			# Set item1 to be the representative
			self.sets[item2_parent-1].parent = self.sets[item1_parent-1].parent
			self.sets[item1_parent-1].rank += 1

		elif item1_parent_rank > item2_parent_rank:
			# Set item1 to be the representative
			self.sets[item2_parent-1].parent = self.sets[item1_parent-1].parent
		else:
			# Set item2 to be the representative
			self.sets[item1_parent-1].parent = self.sets[item2_parent-1].parent

		#print()

	def find_parent(self, num):
		# Array is 0-based, but N begins at 1
		if self.sets[num-1].parent == num:
			return num
		else:
			# Path compression here
			parent = self.find_parent(self.sets[num-1].parent)
			self.sets[num-1].parent = parent
			return parent






# Testing
N = 5
in_str1 = ['1 6', '2 7', '3 8', '4 9', '2 6']

set1 = Disjoint_Set()
set1.make_set(N)


for i in range(N):
	G, B = (int(temp) for temp in in_str1[i].strip().split())
	set1.union(G, B)


# print(set1.nodes_in_set())
# print(set1.get_counts())
print(set1.get_results())

