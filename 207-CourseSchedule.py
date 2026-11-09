class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        indegree=[]
        graph=[]
        for i in range(numCourses):
            indegree.append(0)
            graph.append([])
            
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        count=0
        while queue:
            current=queue.popleft()
            count+=1
            for neighbours in graph[current]:
                indegree[neighbours]-=1
                if indegree[neighbours]==0:
                    queue.append(neighbours)

        if count==numCourses:
            return True
        return False
    
def dfs(graph,node,state):
    if state[node]==1:
        return False
    if state[node]==2:
        return True
    
    state[node]=1

    for neighbours in graph[node]:
        if dfs(graph,neighbours,state)==False:
            return False

    state[node]=2
    return True
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph=[]
        for i in range(numCourses):
            graph.append([])
        for a,b in prerequisites:
            graph[b].append(a)
        
        state=[]
        for i in range(numCourses):
            state.append(0)

        for i in range(numCourses):
            if state[i]==0:
                if dfs(graph,i,state)==False:
                    return False
        return True        