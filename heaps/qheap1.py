"""
This question is designed to help you get a better understanding
of basic heap operations. You will be given queries of 3 types:

"1 v" - Add an element v to the heap.
"2 v" - Delete the element v from the heap.
"3" - Print the minimum of all the elements in the heap.

NOTE: It is guaranteed that the element to be deleted will be there
in the heap. Also, at any instant, only distinct elements will be
in the heap.

Input Format:
The first line contains the number of queries, Q. 
Each of the next Q lines contains a single query of any one of the
3 above mentioned types.

Output Format:
For each query of type 3, print the minimum value on a single line.
"""


class Heap:
	def __init__(self):
		self.heap = []
		self.min = 100000

	def add(self, value):
		self.heap.append(value)

		if value < self.min:
			self.min = value

	def delete(self, value):
		self.heap.remove(value)

		if value == self.min:
			if (len(self.heap) > 0):
				self.min = min(self.heap)
			else:
				self.min = 100000

	def print_min(self):
		print(self.min)






# Q = int(input().strip())

Q = 5
in_str = ['1 4', '1 9', '3', '2 4', '3']

heap = Heap()
for i in range(Q):
	# query = input().strip()
	query = in_str[i]

	try:
		query_type, value = (int(temp) for temp in query.split(' '))
	except:
		query_type = int(query.strip())

	if query_type == 1:
		heap.add(value)
	elif query_type == 2:
		heap.delete(value)
	else:
		heap.print_min()

