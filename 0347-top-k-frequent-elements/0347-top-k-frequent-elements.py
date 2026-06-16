class Solution(object):
    def topKFrequent(self, nums, k):
        
        data = {}

        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        
        answer = []
        sorted_data = sorted(data.items(), key = lambda x : x[1], reverse = True)

        for i in range(k):
            answer.append(sorted_data[i][0])

        return answer
        