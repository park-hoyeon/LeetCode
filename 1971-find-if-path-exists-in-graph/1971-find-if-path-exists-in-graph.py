class Solution(object):
    def validPath(self, n, edges, source, destination):
        
        graph = [[] for _ in range(n)]
        visited = [False] * (n+1)

        for i in edges:
            start = i[0]
            end = i[1]
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(x):
            visited[x] = True

            for i in graph[x]:
                if not visited[i]:
                    dfs(i)
        
        dfs(source)

        return visited[destination]

        