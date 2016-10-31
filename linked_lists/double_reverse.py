"""
Reverse a doubly linked list
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


def Reverse(head):
	if head is None:
		return None

	tail = head.next
	head.next = head.prev
	head.prev = tail

	if tail is not None:
		return Reverse(tail)
	else:
		return head





node2 = Node(2)
node4 = Node(4)
node6 = Node(6)

node2.next = node4
node4.next = node6
node4.prev = node2
node6.prev = node4

print('Original list: ')
print_list(node2)
print()
rev = Reverse(node2)
print_list(rev)



