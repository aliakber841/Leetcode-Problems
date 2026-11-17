from collections import deque
class Solution(object):
    def shortestBridge(self, grid):
        n=len(grid)
        queue=deque()
        start_row=-1
        start_col=-1

        def dfs(row,col):
            if row<0 or row>=n or col<0 or col>=n:
                return
            if grid[row][col]!=1:
                return
            grid[row][col]=2
            queue.append((row,col))
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)

        # Step 1: find the first land cell
        found=False
        for i in range(n):
            if found==True:
                break
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
                    found=True
                    break
        # Step 02: BFS
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        flips=0
        while queue:
            length=len(queue)
            for _ in range(length):
                row,col=queue.popleft()
                for dr,dc in directions:
                    new_row=row+dr
                    new_col=col+dc
                    if new_row<0 or new_row>=n or new_col<0 or new_col>=n:
                        continue
                    if grid[new_row][new_col]==1:
                        return flips
                    if grid[new_row][new_col]==0:
                        grid[new_row][new_col]=2
                        queue.append((new_row,new_col))   
            flips+=1  
        return flips   