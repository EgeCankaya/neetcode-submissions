class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in close:
                if stack and close[c] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        return True if not stack else False 
