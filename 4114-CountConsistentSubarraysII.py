class Solution(object):
    def countConsistent(self, nums):
        n=len(nums)
        result=0
        groups=[]
        lastValue={}
        for i in range(n):
            num=nums[i]
            lastValue[num]=i
            newGroups=[]
            for j in groups:
                currentAnd=j[0] & num
                if len(newGroups)>0 and newGroups[-1][0]==currentAnd:
                    newGroups[-1][2]=j[2]
                else:
                    newGroups.append([currentAnd,j[1],j[2]])

            if len(newGroups)>0 and newGroups[-1][0]==num:
                newGroups[-1][2]=i
            else:
                newGroups.append([num,i,i])

            groups=newGroups
            for g in groups:
                current=g[0]
                if current in lastValue:
                    val=lastValue[current]
                    if val>=g[1]:
                        if val<g[2]:
                            result+=val-g[1]+1
                        else:
                            result+=g[2]-g[1]+1
                    
        return result