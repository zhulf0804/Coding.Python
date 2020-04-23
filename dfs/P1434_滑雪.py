# https://www.luogu.com.cn/problem/P1434

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(i, j, visited):
    mmax = 1
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        if heights[x][y] >= heights[i][j]:
            continue
        if not visited[x * C + y]:
            visited[x * C + y] = 1
            length[x * C + y] = dfs(x, y, visited)
        mmax = max(mmax, 1 + length[x * C + y])
    return mmax


R, C = list(map(int, input().split()))
heights = []
for i in range(R):
    line = list(map(int, input().split()))
    heights.append(line)

visited = [0] * (R * C)
length = [0] * (R * C)
ans = 1


for i in range(R):
    for j in range(C):
        if not visited[i * C + j]:
            #print(i, j)
            visited[i * C + j] = 1
            length[i * C + j] = dfs(i, j, visited)
        #print(i, j, length[i * C + j])
        ans = max(length[i * C + j], ans)
print(ans)
