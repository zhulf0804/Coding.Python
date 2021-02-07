class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) >= 2:
            return False

        if len(first) == len(second):
            is_diff = False
            for i in range(len(first)):
                if first[i] != second[i]:
                    if is_diff:
                        return False
                    is_diff = True
            return True
        if len(first) == len(second) + 1:
            first, second = second, first

        is_add = False
        i, j = 0, 0
        while i < len(first):
            if first[i] == second[j]:
                i += 1
                j += 1
            else:
                if is_add:
                    return False
                is_add = True
                j += 1
        return True
