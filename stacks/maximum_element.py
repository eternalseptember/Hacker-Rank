"""
You have an empty sequence, and you will be given N queries.
Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

Input Format:
The first line of input contains an integer, N.
The next N lines each contain an above mentioned query.
(It is guaranteed that each query is valid.)
"""


class Stack:
	# class variable, because only one stack is necessary
	stack = []
	maxNum = 0

	def push(self, item):
		self.stack.append(item)
		if item > self.maxNum:
			self.maxNum = item

	def pop(self):
		item = self.stack.pop()

		if self.maxNum == item:
			if len(self.stack) > 0:
				self.maxNum = max(self.stack)
			else:
				self.maxNum = 0

		return item

	def print_item(self):
		print(self.maxNum)


stack = Stack()
# n = int(input())

n = 10
test_seq = ['1 97', '2', '1 20', '2', '1 26', '1 20', '2', '3', '1 91', '3']

for i in range(n):
	# query = input()
	try:
		# queryType, x = (int(temp) for temp in query.split(' '))
		queryType, x = (int(temp) for temp in test_seq[i].split(' '))
	except ValueError:
		# queryType = int(query)
		queryType = int(test_seq[i])


	if queryType == 1:
		stack.push(x)
	elif queryType == 2:
		stack.pop()
	else:
		stack.print_item()
