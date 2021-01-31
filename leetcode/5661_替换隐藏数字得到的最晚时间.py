class Solution:
    def maximumTime(self, time: str) -> str:
        ans = ''
        for i in range(5):
            if time[i] != '?':
                ans += time[i]
                continue
            if i == 0:
                if time[1] in ['0', '1', '2', '3', '?']:
                    ans += '2'
                else:
                    ans += '1'
            elif i == 1:
                if ans[0] == '1' or ans[0] == '0':
                    ans += '9'
                else:
                    ans += '3'
            elif i == 3:
                ans += '5'
            elif i == 4:
                ans += '9'
        return ans