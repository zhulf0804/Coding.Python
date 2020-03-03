n = int(input())
ss = list(map(int, input().strip().split()))
cs = list(map(int, input().strip().split()))

dp = [[float('inf')] * 4 for _ in range(n + 1)]
for i in range(1, n+1):
    dp[i][1] = cs[i-1]


for i in range(2, n + 1):
    for j in range(2, 4):
        s, c = ss[i-1], cs[i-1]
        for k in range(1, i):
            if ss[k-1] < s:
                dp[i][j] = min(dp[i][j], dp[k][j-1] + c)
        #print(i, j, dp[i][j])


mmin = float('inf')
for i in range(1, 1+n):
    mmin = min(mmin, dp[i][3])

if mmin == float('inf'):
    print(-1)
else:
    print(mmin)