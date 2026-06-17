class Solution(object):
    def findTheDifference(self, s, t):
        
        data = {}

        for i in s:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        
        for j in t:
            if j not in data or data[j] == 0:
                return j
            
            data[j] -= 1

