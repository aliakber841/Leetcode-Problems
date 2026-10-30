class Solution(object):
    def maxProduct(self, nums):
        if len(nums)==1:
            return nums[0]
        answer=[0]*len(nums)
        smallest=[0]*len(nums)
        answer[0]=nums[0]
        smallest[0]=nums[0]
        result=nums[0]

        for i in range(1,len(nums)):
            option1=nums[i]
            option2=nums[i]*answer[i-1]
            option3=nums[i]*smallest[i-1]

            biggest=option1
            if option2>biggest:
                biggest=option2
            if option3>biggest:
                biggest=option3

            lowest=option1
            if option2<lowest:
                lowest=option2
            if option3<lowest:
                lowest=option3

            answer[i]=biggest
            smallest[i]=lowest

            if answer[i]>result:
                result=answer[i]
        return result