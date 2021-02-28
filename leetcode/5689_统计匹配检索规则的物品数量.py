from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for type, color, name in items:
            f1 = ruleKey == "type" and ruleValue == type
            f2 = ruleKey == "color" and ruleValue == color
            f3 = ruleKey == "name" and ruleValue == name
            if f1 or f2 or f3:
                ans += 1
        return ans