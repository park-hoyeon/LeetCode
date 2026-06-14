from collections import deque

class Solution(object):
    def shortestBridge(self, grid):
       
        n = len(grid)
        m = len(grid[0])

        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        q = deque()
        found = False

        def dfs(x, y):
            if x <= -1 or y <= -1 or x >= n or y >= m:
                return False
            
            if grid[x][y] == 1:
                # 첫 번째 섬을 2로 바꿔서 방문 처리
                grid[x][y] = 2

                # 첫 번째 섬의 모든 칸을 BFS 시작점으로 넣음
                q.append((x, y, 0))

                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

                return True
            
            return False

        # 첫 번째 섬 하나만 찾기
        for i in range(n):
            if found:
                break
            
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
        
        # 첫 번째 섬 전체에서 BFS 시작
        while q:
            x, y, dist = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                
                # 바다라면 다리로 확장
                if grid[nx][ny] == 0:
                    grid[nx][ny] = 2
                    q.append((nx, ny, dist + 1))
                
                # 두 번째 섬을 만나면 현재까지 뒤집은 0의 개수 반환
                if grid[nx][ny] == 1:
                    return dist