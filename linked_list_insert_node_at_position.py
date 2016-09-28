"""
Insert Node at a specific position in a linked list
head input could be None as well for empty list
Node is defined as

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

return back the head of the linked list in the below method.
"""


class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node


def InsertNth(head, data, position):
	newNode = Node(data)

	if head is None or (position == 0):
		newNode.next = head
		return newNode
	else:
		# travel to position
		tail = head
		for i in range(1, position):
			tail = tail.next

		# insert node
		newNode.next = tail.next
		tail.next = newNode

		return head
