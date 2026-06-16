class Solution(object):
    def allPathsSourceTarget(self, graph):
        
        answer = []
        n = len(graph)

        def dfs(x,path):
            
            if x == n-1:
                answer.append(path[:])
                return
            
            for nx in graph[x]:
                path.append(nx)
                dfs(nx,path)
                path.pop()
        
        dfs(0,[0])
    
        return answer