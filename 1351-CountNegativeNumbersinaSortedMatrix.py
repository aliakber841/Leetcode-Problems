class Solution(object):
    def countNegatives(self, grid):
        count=0
        n=len(grid[0])
        for i in range(len(grid)):
            for j in range(n):
                left=0
                right=n
                while left<right:
                    mid=left+(right-left)//2
                    if grid[i][mid]<0:
                        right=mid
                    else:
                        left=mid+1
            count+=n-left
        return count        
    
class Solution(object):
    def countNegatives(self, grid):
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    count+=1
        return count        