# Optimal Solution
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
        previous=head
        current=head.next
        while current is not None:
            if previous.val==current.val:
                temp=current.next
                previous.next=temp
                current=temp
            else:
                previous=current
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