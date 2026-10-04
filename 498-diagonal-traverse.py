class Solution(object):
    def findDiagonalOrder(self, mat):
        m=len(mat)
        n=len(mat[0])
        i=0
        j=0
        count=0
        total=m*n
        result=[]
        while count<total:
            result.append(mat[i][j]) # print ist element of first row
            count+=1
            while i-1>=0 and j+1<n: # check upper diagonal
                j+=1
                i-=1 
                result.append(mat[i][j])
                count+=1
            
            # reached top or last column, move to the start of the next diagonal
            if j+1<n:
                j+=1
            else:
                i+=1
            if count==total:
                break

            result.append(mat[i][j])
            count+=1

            while i+1<m and j-1>=0: #check lower diagonal
                i+=1
                j-=1 
                result.append(mat[i][j])
                count+=1
            # reached last row or first column, move to the start of the next diagonal
            if i+1<m:
                i+=1
            else:
                j+=1
        return result