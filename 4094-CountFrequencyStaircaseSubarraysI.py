class Solution(object):
    def countStaircase(self, nums):
        answer=0
        for i in range(len(nums)):
            result=[]
            hash_frequencies={}
            hash_index={}
            for j in range(i,len(nums)):
                current=nums[j]
                if current not in hash_frequencies:
                    hash_frequencies[current]=1
                    result.append(current)
                    hash_index[current]=len(result)
                else:
                    hash_frequencies[current]+=1

                if hash_frequencies[current]>hash_index[current]:
                    break

                k=len(result)
                length=j-i+1
                
                if length==k*(k+1)//2:
                    answer+=1
        return answer