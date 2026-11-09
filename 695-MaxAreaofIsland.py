from collections import deque
def bfs(grid,row,col):
    queue=deque()
    queue.append((row,col))
    grid[row][col]=0
    area=0

    while queue:
        r,c=queue.popleft()
        area+=1
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        for d in directions:
            newrow=r+d[0]
            newcol=c+d[1]
            if newrow>=0 and newrow<len(grid) and newcol>=0 and newcol<len(grid[0]):
                if grid[newrow][newcol]==1:
                    grid[newrow][newcol]=0
                    queue.append((newrow,newcol))
    return area
class Solution(object):
    def maxAreaOfIsland(self, grid):
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count=bfs(grid,i,j)
                    if result<count:
                        result=count
        return result

        
def dfs(grid,row,col):
    if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]):
        return 0
    if grid[row][col]==0:
        return 0

    grid[row][col]=0

    up=dfs(grid,row-1,col) #up
    down=dfs(grid,row+1,col) #down
    left=dfs(grid,row,col-1) #left
    right=dfs(grid,row,col+1) #right

    return 1+up+down+left+right
class Solution(object):
    def maxAreaOfIsland(self, grid):
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count=dfs(grid,i,j)
                    if result<count:
                        result=count
        return result