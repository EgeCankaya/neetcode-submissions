class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        i = -1
        check = True
        c = 0
        while check:
            if abs(i) <= len(self.stack) and self.stack[i] <= price:
                c += 1
                i -= 1
            else:
                check = False
        
        i = -1
        return c
            
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price) 