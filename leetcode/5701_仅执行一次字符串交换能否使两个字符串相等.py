class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        l = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                l.append(i)
        if len(l) == 0:
            return True
        if len(l) == 2:
            i, j = l
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
            else:
                return False
        return False