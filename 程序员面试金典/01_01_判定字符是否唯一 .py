class Solution:
    def isUnique(self, astr: str) -> bool:
       if len(astr) - len(set(astr)) == 0:
           return True
       return False