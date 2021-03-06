"""
Insert Node at the end of a linked list
head pointer input could be None as well for empty list
Node is defined as

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

return back the head of the linked list in the below method
"""


class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node


def Insert(head, data):
	if head is None:
		head = Node(data)
	else:
		tail = head
		while tail.next is not None:
			tail = tail.next
		tail.next = Node(data)
	return head
