class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2, n+1):
            ans = (ans + m) % i
        return ans


'''
1 <= n <= 10^5
1 <= m <= 10^6
'''