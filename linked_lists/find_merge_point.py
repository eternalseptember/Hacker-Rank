"""
Find the node at which both lists merge and return the data of that node.
head could be None as well for empty list
Node is defined as

class Node(object):
	def __init__(self, data=None, next_node=None):
	self.data = data
	self.next = next_node
"""


def FindMergeNode(headA, headB):
	list = []
	while headA is not None:
		list.append(headA.data)
		headA = headA.next

	# It is guaranteed that the two head nodes will be
	# different and not null.
	headB = headB.next
	while headB is not None:
		if headB.data in list:
			index = list.index(headB.data)
			tail = headB.next

			# possible merge point?
			# check if next item in both lists are null or out of index
			if (tail is None) and (index >= (len(list) - 1)):
				return headB.data
			elif tail.data == list[index + 1]:
				return headB.data

		headB = headB.next
