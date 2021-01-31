class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a, self.b = [], []


    def push(self, x: int) -> None:
        self.a.append(x)
        if not self.b or x < self.b[-1]:
            self.b.append(x)
        else:
            self.b.append(self.b[-1])

    def pop(self) -> None:
        self.a.pop()
        self.b.pop()

    def top(self) -> int:
        return self.a[-1]

    def min(self) -> int:
        return self.b[-1]