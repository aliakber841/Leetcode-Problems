class Solution(object):
    def maxProductPair(self, nums, target):
        result=[]
        hash_table={}
        for i in range(len(nums)):
            remainder=target-nums[i]
            if remainder in hash_table:
                other=hash_table[remainder]
                if nums[i]>nums[other]:
                    result.append(i)
                    result.append(other)
                elif nums[other]>nums[i]:
                    result.append(other)
                    result.append(i)
            hash_table[nums[i]]=i

        if len(result)==0:
            return [-1,-1]

        max_index1=result[0]
        max_index2=result[1]
        maximum=nums[max_index1]*nums[max_index2]
        for i in range(0,len(result),2):
            index1=result[i]
            index2=result[i+1]
            product=nums[index1]*nums[index2]
            if product>maximum:
                maximum=product
                max_index1=index1
                max_index2=index2
        
        return [max_index1,max_index2]      