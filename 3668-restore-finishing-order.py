class Solution(object):
    def recoverOrder(self, order, friends):
        result=[]
        for i in range(0,len(order)):
            if order[i] in friends:
                result.append(order[i])
        return result