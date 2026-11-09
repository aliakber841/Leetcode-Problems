class Solution(object):
    def minOperations(self, nums, locked, k):
        count=0
        maximumPrefix=0
        n=len(nums)
        for i in range(n):
            if locked[i]==1:
                if nums[i]!=i+1 or maximumPrefix!=i:
                    count+=1
            if nums[i]>maximumPrefix:
                maximumPrefix=nums[i]
        if count>k:
            return -1

        invert=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    invert+=1

        return count+invert

class Solution(object):
    def minOperations(self, nums, locked, k):
        count=0
        maximumPrefix=0
        n=len(nums)
        for i in range(n):
            if locked[i]==1:
                if nums[i]!=i+1 or maximumPrefix!=i:
                    count+=1
            if nums[i]>maximumPrefix:
                maximumPrefix=nums[i]
        if count>k:
            return -1

        binaryTree=[0]*(n+1)
        invert=0
        for i in range(n-1,-1,-1):
            position=nums[i]-1
            while position>0:
                invert=invert+binaryTree[position]
                position=position-(position & -position)

            position=nums[i]
            while position<=n:
                binaryTree[position]=binaryTree[position]+1
                position=position+(position & -position)

        return count+invert