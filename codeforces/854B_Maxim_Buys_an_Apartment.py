n, k = list(map(int, input().split()))

if k == 0 or k == n:
    print(0, 0)
else:
    mmin = 1
    mmax = 2 * k
    if k > n // 3:
        mmax = n - k
    print(mmin, mmax)