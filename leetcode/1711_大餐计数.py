from typing import List
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        d = {}
        for k in deliciousness:
            d[k] = d.get(k, 0) + 1
        ans = 0
        for k, v in d.items():
            for e in range(0, 22):
                l = pow(2, e) - k
                cur = 0
                if k < l:
                    cur = (d[k] * d.get(l, 0)) % (1e9 + 7)
                elif k == l:
                    cur = (d[k] * (d[k] - 1)) // 2 % (1e9 + 7)
                ans += cur
        return int(ans)

deliciousness = [1,3,5,7,9] #[1,1,1,3,3,3,7]
a = Solution()
print(a.countPairs(deliciousness))