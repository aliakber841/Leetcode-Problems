# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def getReverseDigits(nums):
    number=0
    for i in range(len(nums)-1,-1,-1):
        number=number*10+nums[i]
    return number
class Solution(object):
    def addTwoNumbers(self, list1, list2):
        result1=[]
        result2=[]
        while list1:
            result1.append(list1.val)
            list1=list1.next
        while list2:
            result2.append(list2.val)
            list2=list2.next
        l1_reversed=getReverseDigits(result1)
        l2_reversed=getReverseDigits(result2)
        sumDigits=l1_reversed+l2_reversed
        if sumDigits==0:
            return ListNode(0)
        remaining_digits=sumDigits
        resultNode=ListNode()
        resultHead=resultNode
        while remaining_digits>0:
            digit=remaining_digits%10
            remaining_digits=remaining_digits//10
            resultHead.next=ListNode(val=digit)
            resultHead=resultHead.next
        return resultHead.next      