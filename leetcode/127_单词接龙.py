from typing import List
# 层次遍历， 超时, 通过 30/40 个测试用例
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        d = {}
        for word in wordList:
            d[word] = 1
        queue = []
        queue.append(beginWord)
        cur_num = 1
        next_num = 0
        cur_depth = 1
        while queue:
            top = queue.pop(0)
            cur_num -= 1
            for i in range(len(endWord)):
                for j in range(97, 97+26):
                    alpha = chr(j)
                    if top[i] != alpha:
                        new_string = top[:i] + alpha + top[i+1:]
                        if new_string == endWord:
                            return cur_depth + 1
                        if new_string in d:
                            queue.append(new_string)
                            d.pop(new_string)
                            next_num += 1
            if cur_num == 0:
                cur_depth += 1
                cur_num = next_num
                next_num = 0
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

obj = Solution()
print(obj.ladderLength(beginWord, endWord, wordList))

