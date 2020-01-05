import math
n = int(input())

# dp[i] = dp[i // 2] + ... +
# dp[1] = 1
dp = [1] * (n + 1)
dp[1] = 1
for i in range(2, n+1):
    for j in range(1, i // 2 + 1):
        dp[i] += dp[j]
    #print(i, dp[i])
print(dp[n])
