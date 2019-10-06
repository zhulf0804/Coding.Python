class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = "0"

        def mul_simple(num, simple):
            simple_mul = ""
            carry = 0

            for j in range(len(num) - 1, -1, -1):
                mul = int(num[j]) * int(simple) + carry
                simple_mul = str(mul % 10) + simple_mul
                carry = mul // 10
            if carry > 0:
                simple_mul = str(carry) + simple_mul
            return simple_mul

        def add(numa, numb):
            carry = 0
            res = ""
            i, j = len(numa) - 1, len(numb) - 1
            while i >= 0 or j >= 0:
                item_a = int(numa[i]) if i >= 0 else 0
                item_b = int(numb[j]) if j >= 0 else 0
                summ = item_a + item_b + carry
                carry = summ // 10
                res = str(summ % 10) + res
                i -= 1
                j -= 1
            if carry > 0:
                res = str(carry) + res
            return res

        for i in range(len(num2) - 1, -1, -1):
            mul_num1 = mul_simple(num1, num2[i]) + "0" * (len(num2) - 1 - i)
            res = add(mul_num1, res)
        return "0" if "".join(set(res)) == "0" else res

num1 = "123"
num2 = "456"
s = Solution()
print(s.multiply(num1, num2))