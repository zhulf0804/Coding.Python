'''
wrong idea:
行中走不通的，有可能列可以走通
比如 m=38, n=15, k=9
(8, 10) 不能通过(8, 0), (8, 1), (8, 2)过来，
但可以通过(0, 0), ..., (0, 9), (0, 10), (1, 10), ..., (7, 10), (8, 10)过来

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        ans = 0
        for i in range(m):
            add = 0
            for j in range(n):
                tmp, a, b = 0, i, j
                while a:
                    tmp += (a % 10)
                    a = a // 10
                while b:
                    tmp += (b % 10)
                    b = b // 10
                if tmp <= k:
                    ans += 1
                    add += 1
                else:
                    break
            if add == 0:
                break
            print(i, add)
        return ans
'''
class Solution:
    def movingCountCore(self, i, j, k, vst):
        m, n = len(vst), len(vst[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if vst[i][j]:
            return 0
        tmp, a, b = 0, i, j
        while a:
            tmp += (a % 10)
            a = a // 10
        while b:
            tmp += (b % 10)
            b = b // 10
        if tmp > k:
            return 0
        vst[i][j] = 1
        ans = 1 + self.movingCountCore(i-1, j, k, vst) \
              + self.movingCountCore(i+1, j, k, vst) \
              + self.movingCountCore(i, j-1, k, vst) \
              + self.movingCountCore(i, j+1, k, vst)
        return ans

    def movingCount(self, m: int, n: int, k: int) -> int:
        vst = [[0] * n for _ in range(m)]
        ans = self.movingCountCore(0, 0, k, vst)
        return ans


m = 38
n = 15
k = 9
a = Solution()
print(a.movingCount(m, n, k))