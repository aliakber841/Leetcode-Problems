from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        indegree=[]
        for i in range(numCourses):
            indegree.append(0)
        graph=[]
        for i in range(numCourses):
            graph.append([])
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        order=[]  
        while queue: 
            current=queue.popleft() 
            order.append(current)  
            for neighbours in graph[current]:
                indegree[neighbours]-=1
                if indegree[neighbours]==0:
                    queue.append(neighbours)

        if len(order)==numCourses:
            return order
        return []

def dfs(graph,node,state,order):
    if state[node]==1:
        return False
    if state[node]==2:
        return True
    
    state[node]=1
    for neighbours in graph[node]:
        if dfs(graph,neighbours,state,order)==False:
            return False
    
    state[node]=2
    order.append(node)
    return True
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        state=[]
        for i in range(numCourses):
            state.append(0)
        graph=[]
        for i in range(numCourses):
            graph.append([])
        for a,b in prerequisites:
            graph[b].append(a)

        order=[]
        for i in range(numCourses):
            if state[i]==0:
                if dfs(graph,i,state,order)==False:
                    return [] 
       
        order.reverse()
        return order