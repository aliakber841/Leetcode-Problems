# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        resultNode=ListNode()
        resultHead=resultNode
        orignalHead=head
        # Copy of the list
        while head is not None:
            resultHead.next=ListNode(head.val)
            resultHead=resultHead.next
            head=head.next
        resultHead=resultNode.next
        # Reverse the orignal
        previous=None
        current=orignalHead
        while current is not None:
            temp=current.next
            current.next=previous
            previous=current
            current=temp
        # Compare both lists
        current=previous
        while resultHead and current:
            if resultHead.val!=current.val:
                return False
            resultHead=resultHead.next
            current=current.next
        return True

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        previous=None
        current=head
        while current:
            current.previous=previous
            previous=current
            current=current.next
        left=head
        right=previous
        while left and right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.previous
        return True