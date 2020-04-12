# https://nanti.jisuanke.com/t/T1217
# python2 可ac, python3超时

T = int(input())

def dfs(x, y, visited, cur):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if visited[x][y]:
        return 0
    if cur == n * m - 1:
        return 1

    visited[x][y] = 1
    ans1 = dfs(x - 2, y - 1, visited, cur + 1)
    ans2 = dfs(x - 2, y + 1, visited, cur + 1)
    ans3 = dfs(x - 1, y - 2, visited, cur + 1)
    ans4 = dfs(x - 1, y + 2, visited, cur + 1)
    ans5 = dfs(x + 1, y - 2, visited, cur + 1)
    ans6 = dfs(x + 1, y + 2, visited, cur + 1)
    ans7 = dfs(x + 2, y - 1, visited, cur + 1)
    ans8 = dfs(x + 2, y + 1, visited, cur + 1)
    visited[x][y] = 0
    #print(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8)
    return ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7 + ans8

for i in range(T):
    n, m, x, y = list(map(int, input().split()))
    visited = [[0] * m for _ in range(n)]
    #visited = [0] * (n * m)
    ans = dfs(x, y, visited, 0)
    print(ans)