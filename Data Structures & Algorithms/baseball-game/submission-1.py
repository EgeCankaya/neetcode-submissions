class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        tot_sum = 0
        for c in operations:
            if c == "+":
                tot_sum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif c == "D":
                tot_sum += 2 * stack[-1]
                stack.append(stack[-1] * 2)
            elif c == "C":
                tot_sum -= stack[-1]
                stack.pop()
            else:
                stack.append(int(c))
                tot_sum += int(c) 
        return tot_sum

            