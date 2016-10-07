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

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def print_item(self):
		item = 0
		for i in self.stack:
			if i > item:
				item = i

		print(item)


stack = Stack()
# n = int(input())

n = 10
test_seq = ['1 97', '2', '1 20', '2', '1 26', '1 20', '2', '3', '1 91', '3']

for i in range(n):
	try:
		# queryType, x = (int(temp) for temp in input().split(' '))
		queryType, x = (int(temp) for temp in test_seq[i].split(' '))
	except ValueError:
		# queryType = int(input())
		queryType = int(test_seq[i])


	if queryType == 1:
		stack.push(x)
	elif queryType == 2:
		stack.pop()
	else:
		stack.print_item()
