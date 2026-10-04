class Solution(object):
    def generateMatrix(self, n):
        m=n
        n=n
        result=[]
        for k in range(n):
            result.append([0]*n)
        count=1
        start=0

        while m>0 and n>0:
            last_row=start+m-1
            last_col=start+n-1
            matrix=[]
        # first row to end
            i=start
            j=start
            while j<=last_col:
                result[i][j]=count
                count+=1
                j+=1
            j-=1
        # last column to end
            i=start+1
            while i<=last_row:
                result[i][j]=count
                count+=1
                i+=1
            i-=1  
        # last row to end of left
            if m>1:
                j-=1
                while j>=start:
                    result[i][j]=count
                    count+=1
                    j-=1
                j+=1
        # ist row to firstrow-1 end
            if n>1:
                i-=1
                while i>start:
                    result[i][j]=count
                    count+=1
                    i-=1
        
        # same procedure again
            start+=1
            m-=2
            n-=2
        
        return result     