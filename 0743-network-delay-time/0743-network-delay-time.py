import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        
        INF = int(1e9)
        graph = [[] for _ in range(n+1)]

        for x,y,cost in times:
            graph[x].append((y,cost))

        def dijkstra(start):
            dist = [INF] * (n+1)

            q = []
            heapq.heappush(q,(0,start))
            dist[start] = 0

            while q:
                d, now = heapq.heappop(q)

                if dist[now] < d:
                    continue
                
                for next_node, fare in graph[now]:
                    cost = d + fare
                    if cost < dist[next_node]:
                        dist[next_node] = cost
                        heapq.heappush(q,(cost,next_node))
            return dist
        
        dist = dijkstra(k)

        answer = max(dist[1:])
        if answer == INF:
            return -1
        return answer
