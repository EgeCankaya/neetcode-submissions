class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        tot_sum = 0
        for c in operations:
            if c == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(b)
                stack.append(a)
                stack.append(a + b)
                tot_sum += a + b
            elif c == "D":
                a = stack.pop()
                stack.append(a)
                stack.append(a * 2)
                tot_sum += 2 * a
            elif c == "C":
                a = stack.pop()
                tot_sum -= a
            else:
                stack.append(int(c))
                tot_sum += int(c) 
        return tot_sum

            