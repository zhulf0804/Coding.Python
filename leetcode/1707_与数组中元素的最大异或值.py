from typing import List


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str):
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"

    def getMaximizeXor(self, word):
        tree = self.lookup
        if not tree:
            return -1
        d = {'0': '1', '1': '0'}
        ans = 0
        for a in word:
            c = d[a]
            if c in tree:
                tree = tree[c]
                ans += 1
            else:
                tree = tree[a]
            ans = ans << 1
        ans = ans >> 1
        return ans


def val2bin(val):
    val = bin(val)[2:]
    return '0' * (32 - len(val)) + val

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        nums = sorted(nums)
        queries = [(m, x, idx) for idx, (x, m) in enumerate(queries)]
        queries = sorted(queries)
        i, n = 0, len(nums)
        trie = Trie()
        for m, x, idx in queries:
            while i < n and nums[i] <= m:
                s = val2bin(nums[i])
                trie.insert(s)
                i += 1
            res[idx] = trie.getMaximizeXor(val2bin(x))
        return res

a = Solution()
nums = [0,1,2,3,4] #[5,2,4,6,6,3] #
queries = [[3,1],[1,3],[5,6]] #[[12,4],[8,1],[6,3]] #
print(a.maximizeXor(nums, queries))