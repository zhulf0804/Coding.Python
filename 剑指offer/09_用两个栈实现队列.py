class CQueue:

    def __init__(self):
        self.a, self.b = [], []

    def appendTail(self, value: int) -> None:
        self.a.append(value)

    def deleteHead(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        if self.b:
            return self.b.pop()
        return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()