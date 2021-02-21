class Solution:
    def minOperations(self, s: str) -> int:
        mmin = len(s)
        s1 = '01' * (mmin // 2) + '0'
        s2 = '10' * (mmin // 2) + '1'
        summ = 0
        for i in range(len(s)):
            if s[i] != s1[i]:
                summ += 1
        mmin = min(mmin, summ)

        summ = 0
        for i in range(len(s)):
            if s[i] != s2[i]:
                summ += 1
        mmin = min(mmin, summ)
        return mmin