import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    dp = [1] * (n + 1)
    ans = 1

    for i in range(n // 2, 0, -1):
        k = 2
        while k * i <= n:
            if s[k * i - 1] > s[i - 1]:
                dp[i] = max(dp[k * i] + 1, dp[i])
            k += 1
    for i in range(1, n + 1):
        ans = max(dp[i], ans)

    print(ans)