n, r = list(map(int, input().split()))
a = list(map(int, input().split()))


i = 0
ok = True
ans = 0
while i < n:
    #print(i)
    z = min(i + r - 1, n - 1)
    j = max(i - r + 1, 0)
    p = -1
    for k in range(z, j - 1, -1):
        if a[k] == 1:
            p = k
            break
    if p == -1:
        ok = False
        break
    ans += 1
    i = p + r
if ok:
    print(ans)
else:
    print(-1)