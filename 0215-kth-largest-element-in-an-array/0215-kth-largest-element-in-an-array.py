import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        
        data = []
        for i in nums:
            heapq.heappush(data,-i)
        
        answer = 0
        while k != 0:
            answer = heapq.heappop(data)
            k-=1
        
        return -answer

        