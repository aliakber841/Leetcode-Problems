def traverse(graph,visited,neighbours,result): 
    current=neighbours
    if current==len(graph)-1:
        result.append(list(visited))
        return
    for neighbours in graph[current]:
        if neighbours not in visited:
            visited.append(neighbours)
            traverse(graph,visited,neighbours,result)
            visited.pop()
class Solution(object):
    def allPathsSourceTarget(self, graph):
        result=[]
        visited=[0]
        traverse(graph,visited,0,result)
        return result


class Solution(object):
    def allPathsSourceTarget(self, graph):
        result=[]
        queue=deque()
        queue.append([0])
        
        while queue:
            path=queue.popleft()
            current=path[-1]

            if current==len(graph)-1:
                result.append(path)
            else:
                for neighbours in graph[current]:
                    newpath=list(path)
                    newpath.append(neighbours)
                    queue.append(newpath)

        return result