N, V = list(map(int, input().strip().split()))
vs, ws = [], []
for i in range(N):
    v, w = list(map(int, input().strip().split()))
    vs.append(v)
    ws.append(w)

g = [[0] * (V + 1) for i in range(N)]
dp = [0] * (V + 1)
for i in range(N-1, -1, -1):
    v, w = vs[i], ws[i]
    for j in range(V, v-1, -1):
        cur = dp[j - v] + w
        if cur >= dp[j]:
            g[i][j] = 1
        dp[j] = max(dp[j], cur)
    #print(dp)

mmax = V
res = []
#print(g)
for i in range(N):
    if g[i][mmax] == 1:
        res.append(i + 1)
        mmax -= vs[i]
res = [str(item) for item in res]
print(' '.join(res))