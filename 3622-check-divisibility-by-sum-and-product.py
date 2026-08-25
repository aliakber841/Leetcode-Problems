class Solution(object):
    def checkDivisibility(self, n):
        temp=n
        sum_arr=0
        product=1
        while temp>0:
            digit=temp%10
            temp//=10
            sum_arr+=digit 
            product*=digit
        if n%(sum_arr+product)==0:
            return True 
        else:
            return False