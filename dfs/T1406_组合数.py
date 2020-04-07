# https://nanti.jisuanke.com/t/T1406

import copy


n, r = list(map(int, input().split()))
res = []


def dfs(x, cur):
    if len(cur) == r:
        tmp = copy.deepcopy(cur)
        tmp.reverse()
        res.append(tmp)
        return
    if x > n:
        return
    dfs(x + 1, cur)
    dfs(x + 1, cur + [x])

dfs(1, [])
m = len(res)
res = sorted(res, reverse=True)
for i in range(0, m, 1):
    cur = list(map(str, res[i]))
    print(''.join(cur))
