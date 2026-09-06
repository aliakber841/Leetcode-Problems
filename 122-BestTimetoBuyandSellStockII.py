class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            elif prices[i]>min_price:
                max_profit+=prices[i]-min_price
                min_price=prices[i]
        return max_profit