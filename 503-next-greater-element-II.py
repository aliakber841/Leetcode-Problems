class Solution(object):
    def nextGreaterElements(self, nums):
        monotonic_stack=[]
        result=[-1]*len(nums)
        for i in range(2*len(nums)):
            current=nums[i%len(nums)]
            while monotonic_stack and current>nums[monotonic_stack[-1]]:
                index=monotonic_stack.pop()
                result[index]=current
            if i<len(nums):
                monotonic_stack.append(i)
        return result