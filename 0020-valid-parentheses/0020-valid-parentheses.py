class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
           ")": "(",
            "]": "[",
            "}": "{" 
        }

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[i]:
                    return False
            
                stack.pop()
    
        return len(stack) == 0