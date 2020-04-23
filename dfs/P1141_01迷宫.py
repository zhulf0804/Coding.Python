# https://www.luogu.com.cn/problem/P1141


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

''' # ac 80%代码
def dfs(i, j, visited, cur):
    for k in range(len(dx)):
        x, y = i + dx[k], j + dy[k]
        if x < 0 or x >= n or y < 0 or y >= n:
            continue
        if maps[x][y] == maps[i][j]:
            continue
        if visited[x * n + y]:
            continue
        visited[x * n + y] = cur
        dfs(x, y, visited, cur)
'''

def dfs(i, j, visited, cur):
    q = [i * n + j]
    while q:
        i, j = q[-1] // n, q[-1] % n
        flag = True
        for k in range(len(dx)):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if maps[x][y] == maps[i][j]:
                continue
            if visited[x * n + y]:
                continue
            visited[x * n + y] = cur
            q.append(x * n + y)
            flag = False
        if flag:
           q.pop()


n, m = list(map(int, input().split()))
maps = []
for i in range(n):
    maps.append(input())

visited = [0] * (n*n)
cur = 1
for i in range(n):
    for j in range(n):
        if not visited[i * n + j]:
            visited[i * n + j] = cur
            dfs(i, j, visited, cur)
            cur += 1

d = {}
for i in range(n*n):
    v = visited[i]
    d[v] = d.get(v, 0) + 1

for _ in range(m):
    i, j = list(map(int, input().split()))
    v = visited[(i - 1) * n + j - 1]
    print(d[v])
