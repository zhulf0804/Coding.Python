# https://www.luogu.com.cn/problem/P1141
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
mat = []
for _ in range(n):
    mat.append(input())
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
def bfs(i, j, visited):
    q, p = [i * n + j], [i * n + j]
    cur = 0
    while cur < len(q):
        v = q[cur]
        i, j = v // n, v % n
        cur += 1
        for dx, dy in dxy:
            x, y = i + dx, j + dy
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if visited[x * n + y]:
                continue
            if mat[i][j] == mat[x][y]:
                continue
            visited[x * n + y] = 1
            q.append(x * n + y)
            p.append(x * n + y)
    for v in p:
        visited[v] = len(p)

visited = [0] * (n * n)
for i in range(n):
    for j in range(n):
        if not visited[i * n + j]:
            visited[i * n + j] = 1
            bfs(i, j, visited)

for _ in range(m):
    i, j = list(map(int, input().split()))
    print(visited[(i - 1) * n + j - 1])