from typing import List
class Solution_1:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            count = 0
            while i != 0:
                count += i&1
                i = i >> 1
            res.append(count)
        return res

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(num + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i - 1] + 1
        return dp

num = 2
s = Solution()
print(s.countBits(num))
