import collections
class Solution_1:
    def firstUniqChar(self, s: str) -> int:
        d = collections.OrderedDict()
        for item in s:
            d[item] = d.get(item, 0) + 1
        for key, value in d.items():
            if value == 1:
                return s.index(key)
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {item: s.count(item) for item in set(s)}
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
