from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        v2id = {v:id for id, v in enumerate(target)}
        arr2 = [v2id[v] for v in arr if v in v2id]
        if len(arr2) == 0:
            return len(target)
        lenn, dp = 1, [0] * (len(arr2) + 1)
        dp[1] = arr2[0]
        for i, v in enumerate(arr2):
            if v > dp[lenn]:
                lenn += 1
                dp[lenn] = v
            else:
                l, r = 1, lenn - 1
                while l < r:
                    mid = l + (r - l + 1) // 2
                    if dp[mid] >= v:
                        r = mid - 1
                    else:
                        l = mid
                if dp[l] < v:
                    dp[l + 1] = v
                else:
                    dp[l] = v
        return len(target) - lenn

a = Solution()
target = [1,3,8]
arr = [2, 6]
print(a.minOperations(target, arr))