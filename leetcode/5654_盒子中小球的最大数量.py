class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for v in range(lowLimit, highLimit + 1):
            tmp = 0
            while v:
                tmp += (v % 10)
                v = v // 10
            d[tmp] = d.get(tmp, 0) + 1
        ans = 1
        for v in d.values():
            ans = max(ans, v)
        return ans
    