N, V = list(map(int, input().strip().split()))
vs, ws = [], []
for i in range(N):
    v, w = list(map(int, input().strip().split()))
    vs.append(v)
    ws.append(w)


dp = [0] * (V + 1)
cnt = [1] * (V + 1)

for i in range(1, N+1):
    v, w = vs[i-1], ws[i-1]
    for j in range(V, v-1, -1):
        cur = dp[j - v] + w
        if cur > dp[j]:
            cnt[j] = cnt[j - v]
        if cur == dp[j]:
            cnt[j] += cnt[j - v]
        dp[j] = max(dp[j], dp[j - v] + w)

print(cnt[V] % (int(1e9 + 7)))