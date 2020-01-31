## 此方法较难理解，提交超时
## 待自己水平达到了，再回头来看

import copy

N, V = list(map(int, input().strip().split()))
dp = [0] * (V + 1)
prev = [0] * (V + 1)
q = [0] * (V + 1)
for i in range(N):
    v, w, s = list(map(int, input().strip().split()))
    prev = copy.deepcopy(dp)
    for j in range(v):
        hh, tt = 0, -1
        for k in range(j, V+1, v):
            if hh <= tt and (k - q[hh]) // v > s:
                hh += 1
            if hh <= tt:
                dp[k] = max(dp[k], prev[q[hh]] + (k - q[hh]) // v * w)
            while hh <= tt and prev[q[tt]] - (q[tt] - j) // v * w <= prev[k] - (k - j) // v * w:
                tt -= 1
            tt += 1
            q[tt] = k

print(dp[V])