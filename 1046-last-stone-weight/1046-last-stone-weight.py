import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        
        q = []
        for i in stones:
            heapq.heappush(q,-i)
        
        while len(q) > 1:
            n1 = -heapq.heappop(q)
            n2 = -heapq.heappop(q)

            if n1 != n2:
                heapq.heappush(q,-(n1-n2))
        
        if len(q) == 1:
            return -q[0]
        else:
            return 0