from collections import deque
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        indegree=[]
        graph=[]
        prereq=[]
        for i in range(numCourses):
            graph.append([])
            indegree.append(0)
            prereq.append(set())

        for a,b in prerequisites:
            graph[a].append(b)
            indegree[b]+=1

        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            current=queue.popleft()
            for neighbours in graph[current]:
                prereq[neighbours].add(current)
                for p in prereq[current]:
                    prereq[neighbours].add(p)
                indegree[neighbours]-=1
                if indegree[neighbours]==0:
                    queue.append(neighbours)
        
        result=[]
        for u,v in queries:
            if u in prereq[v]:
                result.append(True)
            else:
                result.append(False)
        return result

def dfs(graph,node,state,reach):
    if state[node]==1:
        return 
    state[node]=1
    for neighbours in graph[node]:
        dfs(graph,neighbours,state,reach)
        reach[node].add(neighbours)
        for p in reach[neighbours]:
            reach[node].add(p)
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        state=[]
        graph=[]
        reach=[]
        for i in range(numCourses):
            graph.append([])
            state.append(0)
            reach.append(set())

        for a,b in prerequisites:
            graph[a].append(b)
        
        for i in range(numCourses):
            dfs(graph,i,state,reach)
        
        result=[]
        for u,v in queries:
            if v in reach[u]:
                result.append(True)
            else:
                result.append(False)
        return result