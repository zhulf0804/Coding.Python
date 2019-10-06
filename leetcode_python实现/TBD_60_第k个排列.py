class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        def getAllPermutation(cur, left):
            if not left:
                res.append(cur)
                return
            for i, item in enumerate(left):
                getAllPermutation(cur + item, left[:i] + left[i+1:])
        getAllPermutation('', [str(i) for i in range(1, n+1)])
        #res = sorted(res)
        return res[k-1]

n = 9
k = 13531
s = Solution()
res = s.getPermutation(n, k)
print(res)