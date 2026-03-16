class Solution(object):
    def numberOfSteps(self, num):
        step=0
        while num!=0:
            if num%2==0:
                num=num//2
                step+=1
            elif num%2!=0:
                num=num-1
                step+=1
        return step