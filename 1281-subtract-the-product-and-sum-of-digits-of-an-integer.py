class Solution(object):
    def subtractProductAndSum(self, n):
        product_numbers=1
        sum_numbers=0
        while n>0:
            digit=n%10
            n=n//10
            sum_numbers+=digit
            product_numbers*=digit
        return product_numbers-sum_numbers   