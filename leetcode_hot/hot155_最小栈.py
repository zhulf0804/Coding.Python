class MinStack:
    def __init__(self):
        n = int(3e4 + 5)
        self.stack1, self.stack2 = [0] * n, [0] * n
        self.i = 0

    def push(self, val):
        if self.i == 0:
            self.stack2[self.i] = val
        else:
            self.stack2[self.i] = min(val, self.getMin())
        self.stack1[self.i] = val
        self.i += 1

    def pop(self):
        self.i -= 1

    def top(self):
        return self.stack1[self.i-1]

    def getMin(self):
        return self.stack2[self.i-1]