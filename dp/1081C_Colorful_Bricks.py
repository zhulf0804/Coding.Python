# https://codeforces.com/problemset/problem/1081/C

n, m, k = list(map(int, input().split()))

# dp[i][j] = (m - 1) * dp[i-1][j-1] + dp[i-1][j]
dp = [[0] * (k + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = m
for i in range(2, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = ((m - 1) * dp[i-1][j-1] + dp[i-1][j]) % 998244353
        #print(i, j, dp[i][j])
print(dp[n][k] % 998244353)