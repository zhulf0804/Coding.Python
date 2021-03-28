class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        tmp = []
        while not self.isEmpty() and self.peek() < val:
            tmp.append(self.peek())
            self.pop()
        self.stack.append(val)
        while tmp:
            self.stack.append(tmp.pop())

    def pop(self) -> None:
        if not self.isEmpty():
            self.stack.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def isEmpty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()