n = int(input())
a = list(map(int, input().split()))


res = []
dp = [-1] * n


def helper(i):
    if dp[i] != -1:
        return dp[i]
    cur = True
    std = a[i]
    while i + std < n:
        if a[i] < a[i + std]:
            cur = cur and helper(i + std)
        std += a[i]
    std = a[i]
    while i - std >= 0:
        if a[i] < a[i - std]:
            cur = cur and helper(i - std)
        std += a[i]
    if cur:
        dp[i] = 0
    else:
        dp[i] = 1
    return dp[i]


for i in range(n):
    if helper(i):
        res.append('A')
    else:
        res.append('B')
    #print(i, res)
print(''.join(res))