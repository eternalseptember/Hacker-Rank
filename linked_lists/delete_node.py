"""
Delete Node at a given position in a linked list
Node is defined as

class Node(object):

def __init__(self, data=None, next_node=None):
   self.data = data
   self.next = next_node

return back the head of the linked list in the below method.
"""


def Delete(head, position):
    if position == 0:
        head = head.next
    else:
        tail = head
        # travel to right before node to be deleted
        for i in range(1, position):
            tail = tail.next

        nodeToBeDeleted = tail.next
        nodeAfterDelete = nodeToBeDeleted.next
        tail.next = nodeAfterDelete
    return head
