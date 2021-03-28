class StackOfPlates:

    def __init__(self, cap: int):
        self.stack = []
        self.cap = cap

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if len(self.stack) == 0 or len(self.stack[-1]) == self.cap:
            self.stack.append([])
        self.stack[-1].append(val)

    def pop(self) -> int:
        if self.cap == 0 or len(self.stack) == 0:
            return -1
        val = self.stack[-1].pop()
        if len(self.stack[-1]) == 0:
            self.stack = self.stack[:-1]
        return val

    def popAt(self, index: int) -> int:
        if self.cap == 0 or index >= len(self.stack):
            return -1
        val = self.stack[index].pop()
        if len(self.stack[index]) == 0:
            self.stack = self.stack[:index] + self.stack[index+1:]
        return val


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)