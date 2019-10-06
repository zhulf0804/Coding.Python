class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        if str[0] not in "+-" and not str[0].isdigit():
            return 0
        flag = 1
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        i = 0
        val = 0
        while i < len(str):
            if not str[i].isdigit():
                break
            val = val * 10 + int(str[i])
            i += 1
        val *= flag
        val = max(-2**31, val)
        val = min(2**31 - 1, val)
        return val

str1 = "42"
str2 = "   -42"
str3 = "4193 with words"
str4 = "words and 987"
str5 = "-91283472332"
obj = Solution()
print(obj.myAtoi(str5))





