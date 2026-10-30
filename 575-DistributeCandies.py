class Solution(object):
    def distributeCandies(self, candyType):
        hash_set=set()
        for i in range(len(candyType)):
            hash_set.add(candyType[i])
            
        n=len(candyType)
        if len(hash_set)<n/2:
            return len(hash_set)
        else:
            return n/2

class Solution(object):
    def distributeCandies(self, candyType):
        n=len(candyType)
        return min(n/2,len(set(candyType)))
        