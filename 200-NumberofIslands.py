#BFS
from collections import deque
def bfs(grid,row,col): 
    queue=deque()
    queue.append((row,col))
    grid[row][col]="0"
    while queue:
        current=queue.popleft()
        r=current[0]
        c=current[1]
        # left, right, up, down
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        for d in directions:
            newrow=r+d[0]
            newcol=c+d[1]
            if newrow>=0 and newrow<len(grid) and newcol>=0 and newcol<len(grid[0]):
                if grid[newrow][newcol]=="1":
                    grid[newrow][newcol]="0"
                    queue.append((newrow,newcol))
class Solution(object):
    def numIslands(self, grid):
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    bfs(grid,i,j)
                    result+=1
        return result     
    
#DFS
def dfs(grid,row,col): 
    if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]):
        return
    if grid[row][col]=="0":
        return
    elif grid[row][col]=="1":
        grid[row][col]="0"
        dfs(grid,row,col-1) #left
        dfs(grid,row,col+1) #right
        dfs(grid,row-1,col) #up
        dfs(grid,row+1,col) #down
class Solution(object):
    def numIslands(self, grid):
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(grid,i,j)
                    result+=1
        return result     
    
#DFS
def dfs(grid,row,col,visited): 
    if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]):
        return
    if grid[row][col]=="0" or visited[row][col]==True:
        return
    elif grid[row][col]=="1":
        visited[row][col]=True
        dfs(grid,row,col-1,visited) #left
        dfs(grid,row,col+1,visited) #right
        dfs(grid,row-1,col,visited) #up
        dfs(grid,row+1,col,visited) #down
class Solution(object):
    def numIslands(self, grid):
        result=0
        visited=[]
        for i in range(len(grid)):
            visited.append([])
            for j in range(len(grid[0])):
                visited[i].append(False)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visited[i][j]==False:
                    dfs(grid,i,j,visited)
                    result+=1
        return result     