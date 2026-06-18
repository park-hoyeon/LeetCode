class Solution(object):
    def searchInsert(self, nums, target):
        
        answer = 0

        if target in nums:
            answer = nums.index(target)
        
        else:
            nums.append(target)
            nums.sort()
            answer = nums.index(target)
        
        return answer
        