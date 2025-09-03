class Solution(object):
    def maximumWealth(self, accounts):
        richer=0
        for i in range(len(accounts)):
            count=0
            for j in range(len(accounts[i])):
                count+=accounts[i][j]
            if count>richer:
                richer=count
        return richer