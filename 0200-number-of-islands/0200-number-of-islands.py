class Solution(object):
    def numIslands(self, grid):

        n = len(grid)
        m = len(grid[0])
        
        def dfs(x,y):
            if x <= -1 or x >= n or y <= -1 or y >= m:
                return False
            
            if grid[x][y] == '1':
                grid[x][y] = '0'
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)
                return True
            return False

        answer = 0
        for i in range(n):
            for j in range(m):
                if dfs(i,j) == True:
                    answer += 1
        
        return answer
        