class Solution(object):
    def removeElement(self, nums, val):
        index=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            else:
                nums[index]=nums[i]
                index+=1
        return index