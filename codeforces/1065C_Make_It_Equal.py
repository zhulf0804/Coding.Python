n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

mmin, mmax = h[0], h[0]
d = [0]*200001
for i in range(n):
    cur= h[i]
    d[cur] += 1
    if h[i] < mmin:
        mmin = h[i]
    if h[i] > mmax:
        mmax = h[i]

if n == 1 or mmax == mmin:
    print(0)
else:
    ans = 0
    i = 200000
    cur = k
    while i > mmin:
        if d[i] <= cur:
            d[i - 1] += d[i]
            cur -= d[i]
            i -= 1
        else:
           cur = k
           ans += 1

    print(ans + 1)