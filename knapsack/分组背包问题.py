N, V = list(map(int, input().strip().split()))
VW = []
for i in range(N):
    S = int(input())
    tmp = []
    for j in range(S):
        v, w = list(map(int, input().strip().split()))
        tmp.append([v, w])
    VW.append(tmp)

dp = [0] * (V + 1)
for i in range(N):
    s = len(VW[i])
    for j in range(V, 0, -1):
        for k in range(s):
            v, w = VW[i][k]
            if j >= v:
                dp[j] = max(dp[j], dp[j-v] + w)

print(dp[V])