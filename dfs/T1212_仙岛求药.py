# https://nanti.jisuanke.com/t/T1212
M, N = list(map(int, input().split()))
sx, sy = 0, 0
ex, ey = 0, 0
maps = []
for i in range(M):
    line = input()
    if '@' in line:
        sx = line.index('@')
        sy = i
    if '*' in line:
        ex = line.index('*')
        ey = i
    maps.append(line)

visited = [[0] * N for i in range(M)]


def helper(x, y, visited):
    if x < 0 or x >= N or y < 0 or y >= M:
        return float('inf')
    if visited[y][x]:
        return float('inf')
    if maps[y][x] == '*':
        return 0
    if maps[y][x] == '#':
        return float('inf')
    #print(y, x)
    visited[y][x] = 1
    mmin = float('inf')
    mmin = min(mmin, helper(x + 1, y, visited))
    mmin = min((mmin, helper(x - 1, y, visited)))
    mmin = min(mmin, helper(x, y + 1, visited))
    mmin = min(mmin, helper(x, y - 1, visited))
    visited[y][x] = 0

    return mmin + 1 if mmin != float('inf') else mmin

res = helper(sx, sy, visited)

if res == float('inf'):
    print(-1)
else:
    print(res)