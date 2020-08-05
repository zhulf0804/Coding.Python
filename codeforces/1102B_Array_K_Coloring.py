n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ok, d = True, {}

for item in a:
    d[item] = d.get(item, 0) + 1
    if d[item] > k:
        ok = False
        break

if not ok or n < k:
    print("NO")
else:
    aa = zip(list(range(0, n)), a)
    aa = sorted(aa, key=lambda x: x[1])
    c = 1
    z, res = False, [1] * n
    for i, v in aa:
        res[i] = c
        if c >= k:
            z = True
        c += 1
        c = c % (k + 1)
        if c == 0:
            c += 1
    if z:
        print("YES")
        print(' '.join(map(str, res)))
    else:
        print('NO')