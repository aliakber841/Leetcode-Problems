class Solution(object):
    def canAliceWin(self, nums):
        singleSum=0
        doubleSum=0
        for i in range(len(nums)):
            digit=nums[i]
            if digit//10==0:
                singleSum+=digit
            else:
                doubleSum+=digit
        if singleSum==doubleSum:
            return False
        else:
            return True