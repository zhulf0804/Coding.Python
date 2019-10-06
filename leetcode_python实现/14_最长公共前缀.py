from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lens = [len(str) for str in strs]
        min_lens = min(lens)
        for i in range(min_lens):
            cut_strs = [str[:i+1] for str in strs]
            #print(cut_strs)
            if len(set(cut_strs)) <= 1:
                continue
            else:
                return strs[0][:i]
        return strs[0][:min_lens]

s = Solution()
strs = ["a","b"]
res = s.longestCommonPrefix(strs)
print(res)