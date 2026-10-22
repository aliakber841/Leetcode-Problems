import heapq
class Solution(object):
    def kClosest(self, points, k):
        heap=[]
        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            distance=(x*x)+(y*y)
            heapq.heappush(heap,(distance,i))
        
        result=[]
        for i in range(k):
            value,index=heapq.heappop(heap)
            result.append(points[index])
        
        return result