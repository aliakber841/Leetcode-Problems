class Solution(object):
    def trap(self, heights):
        n=len(heights)
        left_max=[0]*n
        right_max=[0]*n

        left_max[0]=heights[0]
        for i in range(1,n):
            if heights[i]>left_max[i-1]:
                left_max[i]=heights[i]
            else:
                left_max[i]=left_max[i-1]
        
        right_max[n-1]=heights[n-1]
        for i in range(n-2,-1,-1):
            if heights[i]>right_max[i+1]:
                right_max[i]=heights[i]
            else:
                right_max[i]=right_max[i+1]

        result=0
        for i in range(n):
            result+=min(left_max[i],right_max[i])-heights[i]
        return result     