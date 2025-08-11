# O(1) Space Using Floyd Detection Algorithm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False    

# O(n) Space Using Hash Table
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        hash_table={}
        while head not in hash_table:
             if head is None:
                return False
             hash_table[head]=True
             head=head.next
        return True    