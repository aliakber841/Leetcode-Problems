# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
    
        length=0
        current=head
        while current:
            current=current.next
            length+=1

        rotations=k%length
        if rotations==0:
            return head
        current=head

        while current.next:
            current=current.next
        current.next=head
        nodeToRotate=length-rotations-1
        count=0
        while count<nodeToRotate:
            head=head.next
            count+=1
        newHead=head.next
        head.next=None
        return newHead  