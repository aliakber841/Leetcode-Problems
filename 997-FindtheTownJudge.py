# In and out degree (graph)
class Solution(object):
    def findJudge(self, n, trust):
        score=[0]*(n+1)

        for a,b in trust:
            score[a]-=1
            score[b]+=1
        
        for i in range(1,n+1):
            if score[i]==n-1:
                return i
        return -1

class Solution(object):
    def findJudge(self, n, trust):
        hash_table=set()
        count={}
        for i in range(1,n+1):
            count[i]=0
        
        for i in range(len(trust)):
            hash_table.add(trust[i][0])
            count[trust[i][1]]+=1
        
        for person in range(1,n+1):
            if person not in hash_table and count[person]==n-1:
                return person
        return -1