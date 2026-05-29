class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # This will now ONLY store indices

        for i, t in enumerate(temperatures):
            # Look up the temperature using the index stored in the stack: temperatures[stack[-1]]
            while stack and t > temperatures[stack[-1]]:
                stackI = stack.pop()
                res[stackI] = i - stackI
            
            # Only append the index
            stack.append(i) 
            
        return res