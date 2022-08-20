from typing import List

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         res = []
#         if len(s) < len(p):
#             return res
#         dict_p, dict_s = {}, {}
#         for w in p:
#             dict_p[w] = dict_p.get(w, 0) + 1
#         for i in range(len(p)):
#             dict_s[s[i]] = dict_s.get(s[i], 0) + 1
        
#         def cmp(d1, d2):
#             for w in range(ord('a'), ord('z')+1):
#                 if d1.get(chr(w), 0) !=  d2.get(chr(w), 0):
#                     return False
#             return True
            
#         for i in range(0, len(s)):
#             if cmp(dict_s, dict_p):
#                 res.append(i)
#             dict_s[s[i]] -= 1
#             if i + len(p) < len(s):
#                 dict_s[s[i+len(p)]] = dict_s.get(s[i+len(p)], 0) + 1
#             else:
#                 break
#         return res

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = {}, {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            while right - left  >= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
