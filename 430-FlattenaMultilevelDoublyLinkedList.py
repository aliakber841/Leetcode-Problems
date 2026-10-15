"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        current=head
        stack=[]
        while current:
            if current.child is not None:
                if current.next is not None:
                    stack.append(current.next)
                childCurrent=current.child
                childCurrent.prev=current
                current.next=childCurrent
                current.child=None   
            if current.next is None and stack:
                saved=stack.pop()
                current.next=saved
                saved.prev=current
            current=current.next
        
        return head