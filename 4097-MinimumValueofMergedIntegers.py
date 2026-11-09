class Solution(object):
    def minMergedInteger(self, nums):
        minimum=0
        for i in range(0,len(nums),2):
            ist=str(nums[i])
            second=str(nums[i+1])
            current=int(ist+second)
            if i==0 or current<minimum:
                minimum=current
        return minimum