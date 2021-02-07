class Solution:
    def __init__(self):
        self.ans = 0
    def sumNums(self, n: int) -> int:
        # if n == 1:
        #     return 1
        n > 1 and self.sumNums(n-1)
        self.ans += n
        return self.ans