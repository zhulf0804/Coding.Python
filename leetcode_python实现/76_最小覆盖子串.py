from collections import Counter
# 超时，通过了 226 / 268 个测试用例
class Solution_1:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        counter_t = Counter(t)
        min_len = float('inf')
        res = ""
        for i in range(m):
            counter_s = Counter(s[i:])
            for j in range(m-1, i-1, -1):
                child_len = j - i + 1
                if child_len < n or counter_s & counter_t != counter_t:
                    break
                counter_s -= Counter(s[j])
                if child_len < min_len:
                    min_len = child_len
                    res = s[i:j+1]
        return res

# 二分查找， 超时 通过 256 / 268 个测试用例
class Solution_2:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        counter_t = Counter(t)
        min_len = float('inf')
        res = ""
        for i in range(m):
            left, right = 0, m - 1
            while left < right:
                mid = (left + right) // 2
                if Counter(s[i:mid+1]) & counter_t == counter_t:
                    right = mid
                else:
                    left = mid + 1
            if Counter(s[i:left+1]) & counter_t == counter_t and left - i + 1 < min_len:
                min_len = left - i + 1
                res = s[i:left+1]
        return res

# 滑动窗口,  267 / 268 个通过测试用例
class Solution_3:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        counter_t = Counter(t)
        min_len = float('inf')
        res = ""
        left, right = 0, 0
        while left < m:
            while right < m and Counter(s[left:right+1]) & counter_t != counter_t:
                right += 1
            if right >= m:
                return res
            while left + 1 <= right and (Counter(s[left+1:right+1]) & counter_t) == counter_t:
                left += 1
            if right - left + 1 < min_len:
                min_len = right - left + 1
                res = s[left:right+1]
                #print(res)
            left += 1
        return res

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        counter_t = Counter(t)
        min_len = float('inf')
        windows = {}
        formed = 0
        res = ""
        left, right = 0, 0
        while left < m:
            while right < m:
                if s[right] in t:
                    windows[s[right]] = windows.get(s[right], 0) + 1
                    if windows[s[right]] == counter_t[s[right]]:
                        formed += 1
                        if formed == len(counter_t):
                            break
                right += 1
            if right >= m:
                return res
            while left <= right:
                if s[left] not in t:
                    left += 1
                    continue
                if windows[s[left]] > counter_t[s[left]]:
                    windows[s[left]] -= 1
                    left += 1
                    continue
                break
            if right - left + 1 < min_len:
                min_len = right - left + 1
                res = s[left:right+1]

            windows[s[left]] -= 1
            formed -= 1
            left += 1
            right += 1
        return res




s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
print(obj.minWindow(s, t))






