# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        previous=None
        fast=head
        slow=head
        while fast and fast.next:
            previous=slow
            slow=slow.next
            fast=fast.next.next
        previous.next=slow.next
        del slow
        return head  