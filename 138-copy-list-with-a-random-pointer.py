# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        hash_table={}
        hash_table[None]=None
        orignalHead=head
        while head:
            hash_table[head]=Node(head.val)
            head=head.next
        head=orignalHead
        copyHead=hash_table[head]
        while head:
            hash_table[head].next=hash_table[head.next]
            hash_table[head].random=hash_table[head.random]
            head=head.next
        return copyHead