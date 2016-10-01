"""
Get Node data of the Nth Node from the end.
head could be None as well for empty list
Node is defined as

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

return back the node data of the linked list in the below method.
"""


def GetNode(head, position):
	tail = head
	counter = 1
	while tail.next is not None:
		tail = tail.next
		counter += 1

	thisNode = counter - position
	tail = head
	counter = 1
	while counter < thisNode:
		tail = tail.next
		counter += 1

	return tail.data
