class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        arr = list(range(n))
        ans = 0
        while ans == 0 or arr != perm:
            ans += 1
            arr2 = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    arr2[i] = arr[i // 2]
                else:
                    arr2[i] = arr[n // 2 + (i - 1) // 2]
            arr = arr2

        return ans
