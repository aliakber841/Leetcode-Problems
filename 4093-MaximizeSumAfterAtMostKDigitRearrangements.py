import heapq
class Solution(object):
    def maximizeSum(self, nums, k):
        heap=[]
        for i in range(len(nums)):
            current=nums[i]
            digits=[]
            remaining_digits=current
        
            while remaining_digits>0:
                digit=remaining_digits%10
                digits.append(digit)
                remaining_digits=remaining_digits//10
            
            digits.sort(reverse=True)
            result=0
            
            for digit in digits:
                result=result*10+digit
            maximum=result-current
            heapq.heappush(heap,(-maximum,i,result))

        while k>0 and len(heap)>0:
            value,index,result=heapq.heappop(heap)
            nums[index]=result
            k-=1

        answer=0
        for i in range(len(nums)):
            answer+=nums[i]

        return answer 