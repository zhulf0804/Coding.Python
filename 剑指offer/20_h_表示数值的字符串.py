'''
Reference: https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/
下面的评论
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        is_num, is_eE, is_dot = False, False, False
        for i, item in enumerate(s):
            if item >= '0' and item <= '9':
                is_num = True
            elif item in 'eE':
                if is_eE or i == len(s) - 1 or not is_num:
                    return False
                is_eE = True
                is_num = False
            elif item in '.':
                if is_dot or is_eE:
                    return False
                is_dot = True
            elif item in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            else:
                return False
        if not is_num:
            return False
        return True
