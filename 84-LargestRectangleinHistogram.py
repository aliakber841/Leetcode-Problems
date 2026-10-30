class Solution(object):
    def largestRectangleArea(self, heights):
        result=0
        stack=[]
        stack.append(0)
        for i in range(1,len(heights)+1):
            if i==len(heights):
                current=0
            else:
                current=heights[i]
            while stack and heights[stack[-1]]>current:
                top_stack=stack.pop()
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                current_height=heights[top_stack]*width
                if current_height>result:
                    result=current_height
            stack.append(i)

        return result  