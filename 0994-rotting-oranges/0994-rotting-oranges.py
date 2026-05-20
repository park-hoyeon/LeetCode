from collections import deque

class Solution(object):
    def orangesRotting(self, grid):

        n = len(grid)
        m = len(grid[0])
        
        time = [[0] * m for _ in range(n)]
        
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        time[nx][ny] = time[x][y] + 1
                        q.append((nx,ny))
    
        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                answer = max(answer, time[i][j])
        
        return answer