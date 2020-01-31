import math


N, V = list(map(int, input().strip().split()))
N1 = 0
vs, ws, ss = [], [], []
for i in range(N):
    v, w, s = list(map(int, input().strip().split()))
    k = int(math.floor(math.log2(s)))
    for j in range(k):
        vs.append(v*pow(2, j))
        ws.append(w*pow(2, j))
        N1 += 1
    left = s - pow(2, k) + 1
    if left > 0:
        vs.append(v*left)
        ws.append(w*left)
        N1 += 1

dp = [0] * (V + 1)
for i in range(N1):
    v = vs[i]
    for j in range(V, v-1, -1):
        dp[j] = max(dp[j], dp[j-v] + ws[i])
print(dp[V])