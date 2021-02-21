# class Solution:
#     def isFlipedString(self, s1: str, s2: str) -> bool:
#         if not s1 and not s2:
#             return True
#         for i in range(len(s1)):
#             if s1[i:] + s1[:i] == s2:
#                 return True
#         return False

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1 + s1