class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies=0
        for i in range(len(candies)):
            if candies[i]>max_candies:
                max_candies=candies[i]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_candies:
                candies[i]=True
            else:
                candies[i]=False
        return candies