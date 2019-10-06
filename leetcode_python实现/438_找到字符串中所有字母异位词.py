from typing import List
from collections import Counter
class Solution_1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        for i in range(len(s)):
            if Counter(p) == Counter(s[i:i+len(p)]):
                res.append(i)
        return res

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        res = []
        dict_p = {}
        dict_s = {}
        for item in p:
            dict_p[item] = dict_p.get(item, 0) + 1
        for i in range(len(p)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
        for i in range(len(s)):
            if i == 0:
                if dict_s == dict_p:
                    res.append(i)
            else:
                if i + len(p) - 1 >= len(s):
                    break
                dict_s[s[i-1]] -= 1
                if dict_s[s[i-1]] == 0:
                    dict_s.pop(s[i-1])
                dict_s[s[i + len(p) - 1]] = dict_s.get(s[i + len(p) - 1], 0) + 1
                if dict_s == dict_p:
                    res.append(i)
        return res

s = "cbaebabacd"
p = "abc"
ss = Solution()
print(ss.findAnagrams(s, p))