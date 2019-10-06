from typing import List

# 超时
class Solution_1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        for i in range(len(T)):
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    res[i] = j - i
                    break
        return res

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        for i in range(len(T)-1, -1, -1):
            j = i + 1
            while j < len(T):
                if T[j] > T[i]:
                    res[i] = j - i
                    break
                j = j + res[j] if res[j] > 0 else len(T)
        return res