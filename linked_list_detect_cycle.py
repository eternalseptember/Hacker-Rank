"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

class Node(object):
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next = next_node
"""


def has_cycle(head):
	if head is None:
		return False

	list = []

	while head is not None:
		item = head.data
		if item in list:
			return True
		else:
			list.append(item)
			head = head.next

	return False
