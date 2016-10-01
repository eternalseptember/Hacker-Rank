"""
Merge two linked lists
head could be None as well for empty list
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

	def __str__(self):
		return str(self.data)


def print_list(head):
	if head is not None:
		print(head.data)
		print_list(head.next)


def MergeLists(headA, headB):
	if (headA is None) and (headB is None):
		return None
	elif headA is None:
		return headB
	elif headB is None:
		return headA

	newHead = None
	if (headA.data < headB.data):
		newHead = headA
		headA = headA.next
	else:
		newHead = headB
		headB = headB.next

	tail = newHead

	while (headA is not None) and (headB is not None):
		if headA.data < headB.data:
			tail.next = headA
			headA = headA.next
		else:
			tail.next = headB
			headB = headB.next
		tail = tail.next

	# outside of the while loop, at least one of the list is empty
	if headA is None:
		tail.next = headB
	else:
		tail.next = headA

	return newHead






node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

# node1.next = node2
# node2.next = node3
# node3.next = node4

node1.next = node3
node3.next = node5
node5.next = node6

node2.next = node4
node4.next = node7

print_list(MergeLists(node1, node2))




