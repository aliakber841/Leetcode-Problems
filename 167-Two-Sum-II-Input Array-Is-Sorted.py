class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while left<right:
            current_sum=numbers[left]+numbers[right]
            if current_sum==target:
                return [left+1,right+1]
            elif current_sum<target:
                left+=1
            else:
                right-=1

class Solution(object):
    def twoSum(self, numbers, target):
        hash_table={}
        for i in range(0,len(numbers)):
            remainder=target-numbers[i]
            if numbers[i] in hash_table:
                return [hash_table[numbers[i]]+1,i+1]  
            hash_table[remainder]=i  