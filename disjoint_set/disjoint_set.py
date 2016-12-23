"""
An attempt to implement a disjoint set to be used for problems in this section.
"""


class Element:
	def __init__(self, data=None, parent=None):
		self.data = data

		if parent is None:
			self.parent = self
		else:
			self.parent = parent

	def __str__(self):
		return str(self.data)


class Disjoint_Set:
	def __init__(self):
		self.set = set()
		self.rep = None
		self.rank = 0


	def __str__(self):
		s = ''
		for item in self.set:
			s += str(item) + ' '
		return s


	def __len__(self):
		return len(self.set)


	def make_connected_pair(self, elem1, elem2):
		# If the set was empty when this function was called
		if len(self.set) == 0:
			item1 = Element(elem1)
			item2 = Element(elem2, item1)
			self.set.update((item1, item2))


	def union(self, another_set):
		# merge another set into this set
		self.set.update(another_set.set)
		# may do something about changing the parent pointer after calculating rank


	def find(self, item):
		# if the item is in this disjoint set,
		# then return the representative
		if item in self.set:
			return self.rep





# Testing

pair1 = Disjoint_Set()
pair1.make_connected_pair(2, 3)
print('pair1: {0}'.format(pair1))
print('size of pair1: {0}'.format(len(pair1)))

pair2 = Disjoint_Set()
pair2.make_connected_pair(3, 4)
print('pair2: {0}'.format(pair2))
print('size of pair2: {0}'.format(len(pair2)))

pair1.union(pair2)
print('pair1 after merging pair2: {0}'.format(pair1))



