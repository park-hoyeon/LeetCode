import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        
        INF = int(1e9)
        n = len(heights)
        m = len(heights[0])

        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        def dijkstra(start):
            q = []
            heapq.heappush(q,(0,start[0],start[1]))

            while q:
                d,x,y = heapq.heappop(q)

                if dist[x][y] < d:
                    continue
                
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y

                    if 0<=nx<n and 0<=ny<m:
                        cost = abs(heights[x][y] - heights[nx][ny])
                        new_cost = max(d,cost)

                        if new_cost < dist[nx][ny]:
                            dist[nx][ny] = new_cost
                            heapq.heappush(q,(new_cost,nx,ny))
        dijkstra((0,0))

        return dist[n-1][m-1]