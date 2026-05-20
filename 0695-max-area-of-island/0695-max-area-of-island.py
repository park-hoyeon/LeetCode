from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        n = len(grid)
        m = len(grid[0])

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        def bfs(x,y):
            q = deque()
            q.append((x,y))
            count = 1

            while q:
                x,y = q.popleft()

                grid[x][y] = 0

                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                        continue
                    
                    if grid[nx][ny] == 0:
                        continue
                    
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        count += 1
                        q.append((nx,ny))
            return count
    
        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    answer = max(answer, bfs(i,j))
        
        return answer