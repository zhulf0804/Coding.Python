from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if item == '+':
                    c = a + b
                elif item == '-':
                    c = a - b
                elif item == '*':
                    c = a * b
                elif item == '/':
                    c = abs(a) // abs(b)
                    if a * b < 0:
                        c = -c
                stack.append(c)
                #print(a, item, b, c)
                continue
            stack.append(int(item))
        return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj = Solution()
print(obj.evalRPN(tokens))