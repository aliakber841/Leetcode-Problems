# Optimal Solution
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current=head
        while current and current.next:
            if current.val==current.next.val:
                temp=current.next
                current.next=current.next.next
                del temp
            else:
                current=current.next
        return head     


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        previous=None
        current=head
        stored_value=None
        while current is not None:
            if stored_value is None:
                stored_value=current.val
                previous=current
                current=current.next
            elif current.val==stored_value:
                previous.next=current.next
                del current
                current=previous.next
            else:
                stored_value=current.val
                previous=current
                current=current.next
        return head