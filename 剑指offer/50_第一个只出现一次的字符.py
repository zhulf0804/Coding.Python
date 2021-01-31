from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = OrderedDict()
        for item in s:
            d[item] = d.get(item, 0) + 1
        ans = ' '
        for k, v in d.items():
            if v == 1:
                ans = k
                break
        return ans