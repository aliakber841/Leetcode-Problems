class Solution(object):
    def smallestEvenMultiple(self, n):
        j=1
        while j%2!=0 or j%n!=0:
            j+=1
        return j