'''
题目不难, 有两个坑:
1. str[0] == '+'时, 直接str=str[1:]并继续判断新的str[0]是否是有效数字时，忽略新的str为空的情况，不严谨.
2. 有效数字后可能被很多无效字符隔断，如'.', '*', ' '，所以需要通过遍历截取有效数字.
'''

class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        is_num, flag = False, 1
        if str[0] in '+-':
            if str[0] == '-':
                flag = -1
            str = str[1:]
        ans = 0
        if str and str[0] >= '0' and str[0] <= '9':
            is_num = True
            i = 0
            while i < len(str) and str[i] >= '0' and str[i] <= '9':
                i +=1
            str = str[:i]
            for item in str:
                ans = ans * 10 + int(item)
        MAX, MIN = pow(2, 31) - 1, -pow(2, 31)
        if is_num:
            if flag == 1:
                ans = min(MAX, ans)
            else:
                ans = max(MIN, -ans)
            return ans
        return 0
