n, p, q, r = list(map(int, input().split()))
a = list(map(int, input().split()))

dp1 = [0] * n
for i in range(n):
    if i == 0:
        dp1[i] = p * a[i]
    else:
        dp1[i] = max(dp1[i-1], p * a[i])

dp2 = [0] * n
for i in range(n):
    if i == 0:
        dp2[i] = p * a[i] + q * a[i]
    else:
        dp2[i] = max(q*a[i] + dp1[i], dp2[i-1])

ans = -float('inf')
for i in range(n):
    ans = max(ans, r * a[i] + dp2[i])
print(ans)