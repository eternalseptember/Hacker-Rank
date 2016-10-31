"""
Insert a node into a sorted doubly linked list
head could be None as well for empty list
Node is defined as

class Node(object):
	def __init__(self, data=None, next_node=None, prev_node = None):
		self.data = data
		self.next = next_node
		self.prev = prev_node

return the head node of the updated list
"""


class Node(object):
	def __init__(self, data=None, next_node=None, prev_node=None):
		self.data = data
		self.next = next_node
		self.prev = prev_node

	def __str__(self):
		return str(self.data)


def print_list(head):
	if head is not None:
		print(head.data, end=' ')
		print_list(head.next)


def SortedInsert(head, data):
	if head is None:
		return Node(data)

	currentNode = head
	posFound = False

	while posFound is False:
		# if currentNode's data is smaller than inserted data
		# move to the right
		if currentNode.data < data:
			nextNode = currentNode.next
			if nextNode is None:
				posFound = True
				newNode = Node(data)
				newNode.prev = currentNode
				currentNode.next = newNode
			elif nextNode.data < data:
				currentNode = currentNode.next
			else:
				posFound = True
				newNode = Node(data, nextNode, currentNode)
				currentNode.next = newNode
				nextNode.prev = newNode
		# if currentNode's data is greater than inserted data
		# assuming the head is the first item in the list
		# make a new head
		elif currentNode.data > data:
			posFound = True
			newNode = Node(data, currentNode)
			currentNode.prev = newNode
			head = newNode


	return head







node2 = Node(2)
node4 = Node(4)
node6 = Node(6)

node2.next = node4
node4.next = node6
node4.prev = node2
node6.prev = node4

print('Original list: ', end=' ')
print_list(node2)

insertValues = [3, 1, 5, 7]
head = node2
for val in insertValues:
	print()
	head = SortedInsert(head, val)
	print_list(head)










