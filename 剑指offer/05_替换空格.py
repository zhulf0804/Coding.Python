class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for item in s:
            if item == ' ':
                res += '%20'
            else:
                res += item
        return res