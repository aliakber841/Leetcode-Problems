# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        previous=head
        current=head
        while current.next is not None:
            previous=previous.next
            temp=current.next
            if temp.next is not None:
                current=temp.next
            else:
                current=temp
        return previous  