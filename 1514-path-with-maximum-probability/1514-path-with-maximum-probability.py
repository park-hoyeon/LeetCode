import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        
        graph = [[] for _ in range(n)]

        for (u,v),p in zip(edges,succProb):
            graph[u].append((v,p))
            graph[v].append((u,p))
        
        prob = [0] * n
        prob[start_node] = 1.0

        def dijkstra(start):
            q = []
            heapq.heappush(q,(-1.0,start))

            while q:
                cur_prob, node = heapq.heappop(q)

                cur_prob = -cur_prob

                if node == end_node:
                    return cur_prob
                
                for next_node, edge_prob in graph[node]:
                    new_prob = cur_prob * edge_prob

                    if new_prob > prob[next_node]:
                        prob[next_node] = new_prob
                        heapq.heappush(q,(-new_prob,next_node))
            return 0.0
        return dijkstra(start_node)        