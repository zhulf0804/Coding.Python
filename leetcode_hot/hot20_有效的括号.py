class Solution:
    def isValid(self, s):
        stack, i = [], 0
        mmap = {'(': ')', '[': ']', '{': '}'}
        while i < len(s):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if mmap[t] != s[i]:
                    return False
            i += 1
        if len(stack) == 0:
            return True
        else:
            return False
        