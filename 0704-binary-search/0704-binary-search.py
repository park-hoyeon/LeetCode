class Solution(object):
    def search(self, nums, target):
        
        answer = 0

        if target in nums:
            answer = nums.index(target)
        else:
            return -1
        return answer
        