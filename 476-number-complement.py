class Solution(object):
    def findComplement(self, num):
        return ((2<<int(math.log(max(num,1),2)))-1)-num