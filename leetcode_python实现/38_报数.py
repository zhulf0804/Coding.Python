class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        res = "1"
        for i in range(2, n+1):
            st = 0
            j = 1
            tmp = ""
            while j < len(res):
                if res[j] == res[st]:
                    j += 1
                else:
                    tmp += str(j - st) + res[st]
                    st = j
                    j += 1
            tmp += str(j - st) + res[st]
            res = tmp
        return res


