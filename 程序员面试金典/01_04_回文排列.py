class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        is_odd = False
        for k, v in d.items():
            if v & 1 == 1:
                if is_odd:
                    return False
                is_odd = True
        return True