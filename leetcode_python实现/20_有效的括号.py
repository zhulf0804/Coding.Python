class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        left = ["(", '{', '[']
        right = [')', '}', ']']
        for item in s:
            if item in left:
                stack.append(item)
            elif item in right:
                if stack and stack[-1] in left and left.index(stack[-1]) == right.index(item):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False


s = Solution()
s.isValid("]")