'''
考虑层数:
k 层最多放置: 1 + 3 + 6 + 10 + ... a_k = k * (k + 1) * (k + 2) // 6 个
其中第 k 层 放置: k * (k + 1) // 2 个

二分查找 总数 <= n的最大层数 k, 然后在第k层逐渐增加元素，判别是否到达n; 注意当第k层增加i个元素时,
总量增加 1 + 2 + ... + i个
'''

class Solution:
    def minimumBoxes(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = l + (r - l + 1) // 2
            if mid * (mid + 1) * (mid + 2) // 6 > n:
                r = mid - 1
            else:
                l = mid
        now = l * (l + 1) * (l + 2) // 6
        ans = l * (l + 1) // 2
        step = 1
        while now < n:
            ans += 1
            now += step
            step += 1
        return ans

a = Solution()
print(a.minimumBoxes(15))