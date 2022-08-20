class Solution:
    def core(self, a, b):
        if a == 0:
            return [')' * b]
        if a == b:
            cur = self.core(a-1, b)
            return ['(' + item for item in cur]
        if a < b:
            cur1 = self.core(a-1, b)
            res1 = ['(' + item for item in cur1]
            cur2 = self.core(a, b-1)
            res2 = [')' + item for item in cur2]
            return res1 + res2

    def generateParenthesis(self, n):
        return self.core(n, n)