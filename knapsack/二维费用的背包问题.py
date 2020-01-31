N, V, M = list(map(int, input().strip().split()))
vs, ws, ms = [], [], []
for i in range(N):
    v, m, w = list(map(int, input().strip().split()))
    vs.append(v)
    ms.append(m)
    ws.append(w)

dp = [[0] * (M + 1) for i in range(V + 1)]
for i in range(N):
    for j in range(V, vs[i]-1, -1):
        for k in range(M, ms[i] - 1, -1):
            dp[j][k] = max(dp[j-vs[i]][k-ms[i]] + ws[i], dp[j][k])
    #print(dp)

print(dp[V][M])