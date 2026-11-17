class Solution(object):
    def isMonotonic(self, nums):
        isGreater=False
        isSmaller=False
        val=nums[0]
        if len(nums)==1:
            return True

        j=1
        while j<len(nums) and nums[j]==val:
            j+=1
        if j==len(nums):
            return True

        if nums[j]>=val:
            isGreater=True
        elif nums[j]<=val:
            isSmaller=True
        i=1
        if isGreater:
            while i<len(nums):
                if nums[i]>=val:
                    val=nums[i]
                else:
                    return False
                i+=1
        elif isSmaller:
            while i<len(nums):
                if nums[i]<=val:
                    val=nums[i]
                else:
                    return False
                i+=1
        return True