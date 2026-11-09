def traverse(n,edges,source,destination,start,visited):
    current=start
    if current==destination:
        return True
    for neighbours in edges[current]:
        if neighbours not in visited:
            visited.add(neighbours)
            if traverse(n,edges,source,destination,neighbours,visited)==True:
                return True
    return False
class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph=[]
        for i in range(n):
            graph.append([])
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=set()
        visited.add(source)
        return traverse(n,graph,source,destination,source,visited)    

from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph=[]
        for i in range(n):
            graph.append([])
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited=set()
        queue=deque()
        queue.append(source)
        visited.add(source)

        while queue:
            current=queue.popleft()

            if current==destination:
                return True

            for neighbours in graph[current]:
                if neighbours not in visited:
                    visited.add(neighbours)
                    queue.append(neighbours)
        return False