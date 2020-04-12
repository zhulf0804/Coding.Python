from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num2letter = {}
        num2letter["2"] = ["a", "b", "c"]
        num2letter["3"] = ["d", "e", "f"]
        num2letter["4"] = ["g", "h", "i"]
        num2letter["5"] = ["j", "k", "l"]
        num2letter["6"] = ["m", "n", "o"]
        num2letter["7"] = ["p", "q", "r", "s"]
        num2letter["8"] = ["t", "u", "v"]
        num2letter["9"] = ["w", "x", "y", "z"]
        # [(n-2）* 3, (n-1) * 3)
        res = []
        def letterCombinationsCore(cur, left):
            if not left:
                res.append(cur)
                return
            n = left[0]
            for letter in num2letter[n]:
                letterCombinationsCore(cur + letter, left[1:])
        letterCombinationsCore("", digits)
        return res

digits = "23"
s = Solution()
res = s.letterCombinations(digits)
print(res)