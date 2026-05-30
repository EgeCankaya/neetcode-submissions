class MyQueue:

    def __init__(self):
        self.stack = []
        self.offset = 0
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        a = self.stack.pop(self.offset)
        self.offset += 1
        return a
    def peek(self) -> int:
        return self.stack[self.offset]
    def empty(self) -> bool:
        return 0 == len(self.stack)
    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()