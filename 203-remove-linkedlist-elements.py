# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy_node=ListNode()
        tail=dummy_node
        current=head
        while current is not None:
            if current.val==val:
                current=current.next
            else:
                tail.next=current
                tail=current
                current=current.next
        tail.next=None
        return dummy_node.next    