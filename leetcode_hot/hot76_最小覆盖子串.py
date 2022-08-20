class Solution:
    def minWindow(self, s, t):
        hs, ht = {}, {}
        for item in t:
            ht[item] = ht.get(item, 0) + 1
        i, j = 0, 0
        cnt = 0
        ans, res = 1e8, ''
        while j < len(s):
            hs[s[j]] = hs.get(s[j], 0) + 1
            if hs[s[j]] <= ht.get(s[j], 0):
                cnt += 1
            while i <= j and hs[s[i]] > ht.get(s[i], 0):
                hs[s[i]] -= 1
                i += 1
            if cnt == len(t):
                if j - i + 1 < ans:
                    ans = j - i + 1
                    res = s[i:j+1]
            j += 1
        return res
                
