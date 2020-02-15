n, w = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))

summ = 0
mmax = w
mmin = 0

for i in range(n):
    cur = a[i]
    if cur >= 0:
        summ += cur
        mmax = min(mmax, w - summ)
    else:
        cmp = 0
        if summ + cur < 0:
            cmp = abs(summ + cur)
        mmin = max(mmin, cmp)
        summ += cur

if mmax < mmin:
    print(0)
else:
    print(mmax - mmin + 1)
