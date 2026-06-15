class Solution(object):
    def highestPeak(self, isWater):
        
        n = len(isWater)
        m = len(isWater[0])
        data = []
        graph = [[-1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    data.append((i,j))
                    graph[i][j] = 0
        
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        q = deque(data)

        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0<=nx<n and 0<=ny<m:
                    if graph[nx][ny] == -1:
                        graph[nx][ny] = graph[x][y] + 1
                        q.append((nx,ny))
        return graph
