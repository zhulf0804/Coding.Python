n, a = int(input()), list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]
if a[0] % 2 == 1:
    dp[0][0] = 1

for i in range(1, n):
    if a[i] % 2 == 0:
        continue
    for j in range(i):
        if a[j] % 2 == 1 and (i - j + 1) % 2 == 1:
            if j == 0:
                dp[i][1] = dp[i][1] or 0
                dp[i][0] = dp[i][0] or 1
            else:
                dp[i][1] = dp[i][1] or dp[j-1][0]
                dp[i][0] = dp[i][0] or dp[j-1][1]

if dp[n-1][0]:
    print("Yes")
else:
    print("No")