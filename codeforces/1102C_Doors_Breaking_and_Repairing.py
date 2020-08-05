n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))

if x > y:
    print(n)
elif x <= y:
    a = sorted(a)
    if a[0] > x:
        print(0)
    else:
        ans, i = 0, 0
        while i < n and a[i] <= x:
            ans += 1
            i += 1
        print((ans + 1) // 2)