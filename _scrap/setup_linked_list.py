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


