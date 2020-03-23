import math


n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
mmax = 1

def helper(v, l, r, a):
    while l < r:
        mid = (l + r) // 2
        if a[mid] < v:
            l = mid + 1
        else:
            r = mid
    if a[l] >= v:
        return l
    else:
        return -1


for i in range(1, n):
    cur = math.ceil(a[i] / 2)
    if a[i-1] >= cur:
        dp[i] = dp[i-1] + 1
    #print(i, a[i], dp[i])
    mmax = max(mmax, dp[i])

print(mmax)