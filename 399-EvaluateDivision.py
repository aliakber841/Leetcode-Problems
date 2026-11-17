class Solution(object):
    def calcEquation(self, equations, values, queries):
        index={}
        for i in range(len(equations)):
            u=equations[i][0]
            v=equations[i][1]
            if u not in index:
                index[u]=len(index)
            if v not in index:
                index[v]=len(index)
        n=len(index)

        edges=[]
        for i in range(len(equations)):
            u=index[equations[i][0]]
            v=index[equations[i][1]]
            edges.append((u,v,values[i]))
            edges.append((v,u,1.0/values[i]))
        
        result=[]
        for query in queries:
            start=query[0]
            end=query[1]
            if start not in index or end not in index:
                result.append(-1.0)
                continue

            distance=[]
            for i in range(n):
                distance.append(-1.0)
            distance[index[start]]=1.0

            for step in range(n-1):
                changed=False
                for u,v,w in edges:
                    if distance[u]!=-1.0 and distance[v]==-1.0:
                        distance[v]=distance[u]*w
                        changed=True
                if not changed:
                    break
            result.append(distance[index[end]])
        return result     