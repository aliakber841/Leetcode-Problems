# Two Pointers
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        address1=headA
        address2=headB
        while address1!=address2:
            if address1:
                address1=address1.next
            else:
                address1=headB
            if address2:
                address2=address2.next
            else:
                address2=headA
        return address1
        
# Hash Table
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hash_table={}
        while headA is not None:
            hash_table[headA]=True
            headA=headA.next
        while headB is not None:
            if headB in hash_table:
                return headB
            else:
                headB=headB.next
        return None
        