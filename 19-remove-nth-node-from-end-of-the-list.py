# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next is None:
            return None
        slow=head
        fast=head
        count=1
        orignalHead=head
        while fast and fast.next:
            slow=slow.next
            nthNode=fast.next
            fast=fast.next.next
            if fast is None:
                count+=1
            else:
                count+=2
        nthNode=count-n
        if nthNode==0:
            return orignalHead.next
        traverse=0
        traverseHead=orignalHead
        previous=None
        while traverse<nthNode:
            traverse+=1
            previous=traverseHead
            traverseHead=traverseHead.next
        previous.next=traverseHead.next
        return orignalHead