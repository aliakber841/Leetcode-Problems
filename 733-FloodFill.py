class Solution(object):
    def floodFill(self, image, sr, sc, color):
        value=image[sr][sc]
        if value==color:
            return image

        rows=len(image)
        columns=len(image[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=columns:
                return
            
            if image[r][c]!=value:
                return
            
            image[r][c]=color

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)


        dfs(sr,sc)
        return image

from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        value=image[sr][sc]
        if value==color:
            return image

        rows=len(image)
        columns=len(image[0])
        queue=deque([(sr,sc)])
        image[sr][sc]=color

        while queue:
            r,c=queue.popleft()

            # up
            if r-1>=0 and image[r-1][c]==value:
                image[r-1][c]=color
                queue.append((r-1,c))

            # down
            if r+1<rows and image[r+1][c]==value:
                image[r+1][c]=color
                queue.append((r+1,c))

            # left
            if c-1>=0 and image[r][c-1]==value:
                image[r][c-1]=color
                queue.append((r,c-1))

            # right
            if c+1<columns and image[r][c+1]==value:
                image[r][c+1]=color
                queue.append((r,c+1))

        return image