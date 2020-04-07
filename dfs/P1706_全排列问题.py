# https://www.luogu.com.cn/problem/P1706

import sys
input = sys.stdin.readline
n = int(input())
res = []


def dfs(cur, visited):
    if len(cur) == n:
        res.append(cur)
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = 1
            dfs(cur + [i], visited)
            visited[i] = 0


dfs([], [0] * (n + 1))
for i in range(len(res)):
    cur = res[i]
    print('    ' + '    '.join(list(map(str, cur))))

