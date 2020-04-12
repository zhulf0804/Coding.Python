from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in dict:
                dict[key] = []
            dict[key].append(str)
        res = []
        print(dict)
        for key, val in dict.items():
            res.append(val)
        return res

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

s = Solution()
res = s.groupAnagrams(strs)
print(res)