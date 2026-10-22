import heapq
class MedianFinder(object):

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num):
        heapq.heappush(self.small,-num)
        biggest_small=-heapq.heappop(self.small)
        heapq.heappush(self.large,biggest_small)
        
        if len(self.large)>len(self.small):
            smallest_large=heapq.heappop(self.large)
            heapq.heappush(self.small,-smallest_large)

    def findMedian(self):
        if len(self.small)>len(self.large):
            return float(-self.small[0])
        return (-self.small[0]+self.large[0])/2.0