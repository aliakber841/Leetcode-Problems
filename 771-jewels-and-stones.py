class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        current_stone=""
        count=0
        for i in range(len(stones)):
            current_stone=stones[i]
            if current_stone in jewels:
                count+=1
        return count      