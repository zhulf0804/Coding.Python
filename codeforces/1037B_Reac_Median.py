n, s = list(map(int, input().split()))
a = list(map(int, input().split()))

a = sorted(a)
res = 0
if a[n // 2] == s:
    print(0)
elif a[n // 2] < s:
    for i in range(n // 2, n):
        if a[i] < s:
            res += (s - a[i])
        else:
            break
    print(res)
else:
    for i in range(n // 2, -1, -1):
        if a[i] > s:
            res += (a[i] - s)
        else:
            break
    print(res)