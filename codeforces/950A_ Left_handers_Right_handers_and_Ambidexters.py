line = input()
l, r, a = list(map(int, line.strip().split()))
#print(l, r, a)
mmin = min(l, r)
mmax = max(l, r)

if a + mmin <= mmax:
    print(2 * (a + mmin))
else:
    left = a + mmin - mmax
    print(2 * (mmax + left // 2))