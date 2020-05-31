n, k = list(map(int, input().split()))
ans = 0
for i in [2, 5, 8]:
    cur = n * i
    ans += (cur // k)
    if cur % k != 0:
        ans += 1
print(ans)