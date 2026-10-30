# Approach 1: Staircase
class Solution(object):
    def createGrid(self, m, n):
        result=[]
        for i in range(m):
            start=min(i,n-1)
            if i==m-1:
                end=n-1
            else:
                end=min(i+1,n-1)
            string=""
            for j in range(n):
                if j>=start and j<=end:
                    string+="."
                else:
                    string+="#"
            result.append(string)
        return result
    
# Approach 2: top row + last column
class Solution(object):
    def createGrid(self, m, n):
        result=[]
        for i in range(m):
            string=""
            for j in range(n):
                if i==0:
                    string+="."
                elif j<n-1:
                    string+="#"
                else:
                    string+="."
            result.append(string)

        return result