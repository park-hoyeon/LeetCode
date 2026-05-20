from collections import deque

class Solution(object):
    def updateMatrix(self, mat):

        n = len(mat)
        m = len(mat[0])
        distance = [[-1] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    q.append((i,j))

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < n and 0 <= ny < m:
                    if distance[nx][ny] == -1:
                        distance[nx][ny] = distance[x][y] + 1
                        q.append((nx,ny))
        return distance
