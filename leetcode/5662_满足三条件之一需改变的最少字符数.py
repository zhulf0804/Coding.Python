class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        alphas = [chr(i) for i in range(97,123)]
        ans = 2e5 + 5
        for alpha in alphas:
            ans1, ans2, ans3 = 0, 0, 0
            for item in a:
                if item != alpha:
                    ans1 += 1
                if item > alpha and alpha != 'z':
                    ans2 += 1
                if item < alpha and alpha != 'a':
                    ans3 += 1

            for item in b:
                if item != alpha:
                    ans1 += 1
                if item <= alpha and alpha != 'z':
                    ans2 += 1
                if item >= alpha and alpha != 'a':
                    ans3 += 1
            ans = min(ans, ans1)
            if alpha != 'z':
                ans = min(ans, ans2)
            if alpha != 'a':
                ans = min(ans, ans3)
        return ans

s = Solution()
a = "dabadd"
b = "cda"
print(s.minCharacters(a, b))