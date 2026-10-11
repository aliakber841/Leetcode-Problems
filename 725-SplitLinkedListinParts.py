# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        result=[]
        length=0
        current=head
        while current:
            length+=1
            current=current.next

        split_length=length//k
        extra=length%k
        target=split_length
        if extra>0:
            target+=1
            extra-=1
        
        split=[]
        count=0
        current=head

        while current and k>0:
            split.append(current)
            count+=1  
            current=current.next
            if count==target:
                split[-1].next=None
                result.append(split[0])
                split=[]
                k-=1
                count=0
                target=split_length
                if extra>0:
                    target+=1
                    extra-=1       
        
        while k>0:
            result.append(None)
            k-=1
        return result