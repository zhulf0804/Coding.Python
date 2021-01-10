from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for item in encoded:
            ans = res[-1] ^ item
            res.append(ans)
        return res

encoded = [6,2,7,3]
first = 4
a = Solution()
print(a.decode(encoded, first))