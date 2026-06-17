class Solution(object):
    def findCenter(self, edges):
        
        n = len(edges)
        graph = [[] for _ in range(n+2)]

        for i in edges:
            a = i[0]
            b = i[1]
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(1,n+2):
            if len(graph[i]) == n:
                return i
        
        return graph
        