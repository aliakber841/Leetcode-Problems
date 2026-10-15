# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def gcd(a,b):
    while b!=0:
        remainder=a%b
        a=b
        b=remainder
    return a
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        if head is None or head.next is None:
            return head
        previous=head
        current=head.next
        while previous and current:
            greatest=gcd(previous.val,current.val)
            
            newNode=ListNode()
            newNode.val=greatest
            newNode.next=previous.next
            previous.next=newNode

            previous=current
            current=current.next
        return head     