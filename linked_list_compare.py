"""
Merge two linked list
head could be None as well for empty list
Node is defined as

class Node(object):
	def __init__(self, data=None, next_node=None):
	self.data = data
	self.next = next_node

return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
	if (headA is None) and (headB is None):
		return 1
	elif (headA is None) or (headB is None):
		return 0

	if (headA.data) == (headB.data):
		return CompareLists(headA.next, headB.next)
	else:
		return 0
