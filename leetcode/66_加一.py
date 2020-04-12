from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            summ = digits[i] + 1 if i == len(digits) - 1 else digits[i]
            summ += carry
            digits[i] = summ % 10
            carry = summ // 10
            if carry == 0:
                return digits
        if carry > 0:
            digits.insert(0, carry)
        return digits

s = Solution()
digits = [1, 2, 3]
print(s.plusOne(digits))