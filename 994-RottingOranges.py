from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        queue=deque()
        time=0
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        while queue:
            rottedThisMinute=False
            for k in range(len(queue)):
                row,col=queue.popleft()
                for d in directions:
                    newRow=row+d[0]
                    newCol=col+d[1]
                    if newRow>=0 and newRow<len(grid) and newCol>=0 and newCol<len(grid[0]):
                        if grid[newRow][newCol]==1:
                            grid[newRow][newCol]=2
                            queue.append((newRow,newCol))
                            fresh-=1
                            rottedThisMinute=True
            if rottedThisMinute:
                time+=1
        if fresh>0:
            return -1
        return time 