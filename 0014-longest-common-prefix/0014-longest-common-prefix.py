class Solution(object):
    def longestCommonPrefix(self, strs):
        
        strs.sort()

        a = strs[0]
        b = strs[-1]

        answer = ""

        for i in range(min(len(a),len(b))):
        
            if a[i] == b[i]:
                answer += a[i]
            else:
                break
        
        return answer
        