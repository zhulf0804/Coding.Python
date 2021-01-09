from typing import List

def helper(a, st, v1, v2):
    l1, r1 = st, len(a) - 1
    while l1 < r1:
        mid = (l1 + r1) // 2
        if a[mid] - a[st-1] < v1:
            l1 = mid + 1
        else:
            r1 = mid
    if a[l1] - a[st-1] < v1 or l1 == len(a) - 1:
        return 0

    l2, r2 = st, len(a) - 1
    while l2 < r2:
        mid = l2 + (r2 - l2 + 1) // 2
        if a[mid] - a[st-1] > v2:
            r2 = mid - 1
        else:
            l2 = mid
    if a[l2] - a[st-1] > v2:
        return 0
    l2 = min(len(a) - 2, l2)
    if l1 > l2:
        return 0

    return (l2 - l1 + 1)


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        cur, summ = 0, []
        for num in nums:
            cur += num
            summ.append(cur)
        n, ans = len(nums), 0
        for i in range(n-2):
            lv, rv = summ[i], (summ[n-1] - summ[i]) // 2
            cur = helper(summ, i+1, lv, rv)
            ans += cur
            ans = ans % (1e9 + 7)
        return int(ans)

a = Solution()
nums = [0, 0, 0]
print(a.waysToSplit(nums))