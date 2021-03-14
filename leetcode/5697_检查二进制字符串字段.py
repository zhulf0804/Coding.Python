class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        zero = False
        for item in s:
            if item == '0':
                zero = True
            if zero and item == '1':
                return False
        return True
