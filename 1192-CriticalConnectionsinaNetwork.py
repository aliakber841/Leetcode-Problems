class Solution(object):
    def criticalConnections(self, n, connections):
        graph=[]
        discoverytime=[]
        low=[]
        for i in range(n):
            graph.append([])
            discoverytime.append(-1)
            low.append(-1)

        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)

        time=[0]
        result=[]

        def dfs(current,parent):
            discoverytime[current]=time[0]
            low[current]=time[0]
            time[0]+=1
            for neighbour in graph[current]:
                if neighbour==parent:
                    continue
                if discoverytime[neighbour]==-1: #unvisited
                    dfs(neighbour,current)
                    if low[neighbour]<low[current]: #parent will comapre its low with neighbours and selects low
                        low[current]=low[neighbour]
                    if low[neighbour]>discoverytime[current]: # check for bridge
                        result.append([current,neighbour])
                else: #visited but neighbour is not parent
                    if discoverytime[neighbour]<low[current]: 
                        low[current]=discoverytime[neighbour]

        dfs(0,-1)
        return result