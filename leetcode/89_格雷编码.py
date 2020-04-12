from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        d = {}
        cur = [0] * n
        d[0] = 1
        ind = 1
        res.append(0)
        while ind < 2 ** n:
            for i in range(n):
                cur[i] = cur[i] ^ 1
                val = 2 ** (n - i - 1)
                if cur[i] == 0:
                    val = -val
                val = res[-1] + val
                if val in d:
                    cur[i] = cur[i] ^ 1
                    continue
                else:
                    res.append(val)
                    d[val] = 1
                    ind += 1
                    break
        return res
