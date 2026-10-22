import heapq
class Solution(object):
    def findRelativeRanks(self, score):
        heap=[]
        for i in range(len(score)):
            heapq.heappush(heap,(-score[i],i))

        result=[""]*len(score)
        rank=1

        while heap:
            value,index=heapq.heappop(heap)
            if rank==1:
                result[index]="Gold Medal"
            elif rank==2:
                result[index]=("Silver Medal")
            elif rank==3:
                result[index]=("Bronze Medal")
            else:
                result[index]=str(rank)
            rank+=1
        
        return result