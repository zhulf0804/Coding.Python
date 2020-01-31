# oj: https://www.acwing.com/problem/content/2/


N, V = list(map(int, input().strip().split()))
vs, ws = [], []
for i in range(N):
    v, w = list(map(int, input().strip().split()))
    vs.append(v)
    ws.append(w)

dp = [0] * (V + 1)
for i in range(1, N+1):
    v = vs[i-1]
    for j in range(V, v-1, -1):
        dp[j] = max(dp[j], dp[j-v] + ws[i-1])
print(dp[V])


''' old version
N, V = list(map(int, input().strip().split()))
vs, ws = [], []
for i in range(N):
    v, w = list(map(int, input().strip().split()))
    vs.append(v)
    ws.append(w)

dp = [[0] * (N + 1) for i in range(V + 1)]
for i in range(1, V+1):
    for j in range(1, N+1):
        dp[i][j] = max(dp[i][j], dp[i][j-1])
        if i >= vs[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-vs[j-1]][j-1] + ws[j-1])

print(dp[V][N])
'''