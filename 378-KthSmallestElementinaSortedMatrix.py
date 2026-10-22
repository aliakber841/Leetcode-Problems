class Solution(object):
    def kthSmallest(self, matrix, k):
        n=len(matrix)
        low=matrix[0][0]
        high=matrix[n-1][n-1]
        while low<high:
            mid=(low+high)//2
            count=0
            row=n-1
            col=0
            while row>=0 and col<n:
                if matrix[row][col]<=mid:
                    count+=row+1
                    col+=1
                else:
                    row-=1
            if count<k:
                low=mid+1
            else:
                high=mid
        return low

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap=[]
        rows=len(matrix)
        columns=len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                heapq.heappush(heap,matrix[i][j])
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)