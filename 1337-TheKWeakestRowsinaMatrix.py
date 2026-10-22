import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        rows=len(mat)
        columns=len(mat[0])
        result=[]
        for i in range(rows):
            count=0
            for j in range(columns): 
                if mat[i][j]==1:
                    count+=1
            result.append(count)
        
        heap=[]
        for i in range(len(result)):
            heapq.heappush(heap,(-result[i],-i))    
            if len(heap)>k:
                heapq.heappop(heap)
        
        answer=[]
        while heap:
            count,index=heapq.heappop(heap)
            answer.append(-index)
        answer.reverse()
        return answer