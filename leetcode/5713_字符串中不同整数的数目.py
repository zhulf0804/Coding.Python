class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums, st = [], 0
        n = len(word)
        for i in range(n):
            if word[i] >= '0' and word[i] <= '9':
                continue
            else:
                j = i - 1
                if j >= st:
                    nums.append(int(word[st:j+1]))
                st = i + 1
        if word[n-1] >= '0' and word[n-1] <= '9':
            nums.append(int(word[st:n]))
        return len(set(nums))
