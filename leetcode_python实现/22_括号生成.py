from typing import List
class Solution:
    def generateParenthesis(self, n:int) -> List[str]:
        res = []
        def generateParenthesis(cur, left, right):
            if left > right:
                return
            if left == 0:
                res.append(cur + ")" * right)
                return
            generateParenthesis(cur + "(", left-1, right)
            generateParenthesis(cur + ")", left, right-1)
        generateParenthesis("", n, n)
        return res