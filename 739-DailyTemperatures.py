class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        answer=[0]*len(temperatures)
        
        for i in range(0,len(temperatures)):
            current=temperatures[i]
            while stack and current>temperatures[stack[-1]]:
                    index=stack.pop()
                    answer[index]=i-index
            if i<len(temperatures):
                stack.append(i)
        return answer