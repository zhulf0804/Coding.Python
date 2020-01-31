# oj: https://www.acwing.com/problem/content/4/

N, V = list(map(int, input().strip().split()))
vs, ws, ss = [], [], []
for i in range(N):
    v, w, s = list(map(int, input().strip().split()))
    vs.append(v)
    ws.append(w)
    ss.append(s)

dp = [0] * (V + 1)
for i in range(N):
    v = vs[i]
    for j in range(V, v-1, -1):
        for s in range(min(j // v, ss[i]) + 1):
            dp[j] = max(dp[j], dp[j-s*v] + s*ws[i])
print(dp[V])

'''
N, V = list(map(int, input().strip().split()))
vs, ws, ss = [], [], []
for i in range(N):
    v, w, s= list(map(int, input().strip().split()))
    vs.append(v)
    ws.append(w)
    ss.append(s)

dp = [[[0] * 102 for _ in range(N + 1)] for _ in range(V + 1)]
for i in range(1, V+1):
    for j in range(1, N+1):
        for s in range(1, ss[j-1] + 1):
            dp[i][j][s] = max(dp[i][j][s], dp[i][j-1][ss[j-2]])
            if i >= vs[j-1]:
                if s > 1:
                    dp[i][j][s] = max(dp[i][j][s], dp[i-vs[j-1]][j][s-1] + ws[j-1])
                else:  # 细节问题
                    dp[i][j][s] = max(dp[i][j][s],
                                      dp[i - vs[j - 1]][j-1][ss[j-2]] + ws[j - 1])
            #print(i, j, s, dp[i][j][s])

print(dp[V][N][ss[N-1]])
'''