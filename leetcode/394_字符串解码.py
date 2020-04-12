class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for item in s:
            if item == ']':
                num = ""
                base = ""
                complted = False
                while stack:
                    if complted and (stack[-1].isalpha() or stack[-1] == '['):
                        break
                    top = stack.pop()
                    if top == '[':
                        complted = True
                        continue
                    if not complted and top.isalpha():
                        base = top + base
                        continue
                    if top.isdigit():
                        num = top + num
                stack.append(base * int(num))
            else:
                stack.append(item)
            #print(item, stack)
        return "".join(stack)

#s = "3[a]2[bc]"
#s = "3[a2[c]]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
obj = Solution()
print(obj.decodeString(s))