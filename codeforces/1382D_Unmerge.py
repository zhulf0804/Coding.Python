t = int(input())
for _ in range(t):
    n, p = int(input()), list(map(int, input().split()))
    v, w = [], []
    i, k = 0, 0
    while i < 2*n:
        j = i + 1
        while j < 2 * n and p[j] < p[i]:
            j += 1
        v.append(j - i)
        w.append(j - i)
        k += 1
        i = j
    #print(v)
    dp = [[0] * (n + 1) for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if j >= w[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + v[i-1])
    if dp[k][n] == n:
        print("YES")
    else:
        print("NO")