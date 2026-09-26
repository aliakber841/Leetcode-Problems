def rotate(matrix):
    n=len(matrix)
    for i in range(0,n):
        j=i
        while j<n:
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
            j+=1
        
    for j in range(0,n):
        left=0
        right=n-1
        while left<=right:
            temp=matrix[j][right]
            matrix[j][right]=matrix[j][left]
            matrix[j][left]=temp
            left+=1
            right-=1 
class Solution(object):
    def findRotation(self, mat, target):
        for _ in range(0,4):
            if mat==target:
                return True
            else:
                rotate(mat)
        return False