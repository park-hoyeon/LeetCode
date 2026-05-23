class Solution(object):
    def largestNumber(self, nums):

        str_nums = list(map(str, nums))
        
        str_nums.sort(key=lambda x: x*10, reverse=True)

        answer = ''.join(str_nums)

        return str(int(answer))
        