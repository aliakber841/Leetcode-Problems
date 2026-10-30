class Solution(object):
    def maximalRectangle(self, matrix):
        rows=len(matrix)
        columns=len(matrix[0])
        heights=[0]*columns
        result=0
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]=="1":
                    heights[j]+=1
                elif matrix[i][j]=="0":
                    heights[j]=0
            stack=[]
            stack.append(0)
            for k in range(1,len(heights)+1):
                if k==len(heights):
                    current=0
                else:
                    current=heights[k]
                while stack and current<heights[stack[-1]]:
                    top_stack=stack.pop()
                    if stack:
                        width=k-stack[-1]-1
                    else:
                        width=k
                    current_height=heights[top_stack]*width
                    if current_height>result:
                        result=current_height

                stack.append(k)       
        return result                