import heapq
class Solution(object):
    def kthFactor(self, n, k):
        factors=[]
        i=1
        while i*i<=n:
            if n%i==0:
                factors.append(i)
                other=n//i
                if other!=i:
                    factors.append(other)
            i+=1
        
        if len(factors)<k:
            return -1
        
        heap=[]
        for i in range(len(factors)):
            heapq.heappush(heap,factors[i])
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)      

class Solution(object):
    def kthFactor(self, n, k):
        factors=[]
        i=1
        while i*i<=n:
            if n%i==0:
                factors.append(i)
                other=n//i
                if other!=i:
                    factors.append(other)
            i+=1
        
        if len(factors)<k:
            return -1
        
        factors.sort()
        return factors[k-1]    