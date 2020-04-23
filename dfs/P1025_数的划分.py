# https://www.luogu.com.cn/problem/P1025
# dfs + 剪枝(for循环内剪枝是必须的)

n, k = list(map(int, input().split()))
summ = 0
def dfs(curi, curx, cursum):
    if cursum == n and curi == k:
        return 1
    if curi >= k:
        return 0
    if cursum >= n:
        return 0

    num = 0
    for i in range(curx, (n - cursum) // (k - curi) + 1):
        num += dfs(curi + 1, i, cursum + i)
    return num

ans = 0
for j in range(1, n // k + 1):
    ans += dfs(curi=1, curx=j, cursum=j)
print(ans)