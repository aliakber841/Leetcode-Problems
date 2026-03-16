class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(0,len(nums)):
            target.insert(index[i],nums[i])
        return target
# insert → it builds the target array correctly step by step.