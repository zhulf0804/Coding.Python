class TripleInOne:

    def __init__(self, stackSize: int):
        self.size = stackSize
        self.stack = [[], [], []]

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stack[stackNum]) == self.size:
            return
        self.stack[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        return self.stack[stackNum].pop()

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        return self.stack[stackNum][-1]

    def isEmpty(self, stackNum: int) -> bool:
        if len(self.stack[stackNum]) == 0:
            return True
        return False


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)