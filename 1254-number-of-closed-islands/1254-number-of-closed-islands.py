class Solution(object):
    def closedIsland(self, graph):
        
        n = len(graph)
        m = len(graph[0])

        def dfs(x,y):
            if x <= -1 or x >= n or y <= -1 or y >= m:
                return False
            
            if graph[x][y] == 0:
                graph[x][y] = 1
                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y+1)
                dfs(x,y-1)
                return True
            return False
        
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)
        
        for j in range(m):
            dfs(0,j)
            dfs(n-1,j)
        
        answer = 0
        for i in range(n):
            for j in range(m):
                if dfs(i,j) == True:
                    answer += 1
        
        return answer