class Solution(object):
    def numEnclaves(self, grid):
        
        n = len(grid)
        m = len(grid[0])

        def dfs(x,y):
            if x <= -1 or x >= n or y <= -1 or y >= m:
                return False
            
            if grid[x][y] == 1:
                grid[x][y] = 0
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
                if grid[i][j] == 1:
                    answer += 1
        
        return answer