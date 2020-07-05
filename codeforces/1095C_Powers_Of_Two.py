import math

n, k = list(map(int, input().split()))
binnum = bin(n)[2:]
bits = [int(item) for item in binnum]

if sum(bits) > k or k > n:
    print('NO')
else:
    v, m = sum(bits), len(bits)
    ok = False
    for i in range(m):
        if k == v:
            ok = True
            break
        count = bits[i]
        if i < m - 1:
            if count >= k - v:
                bits[i + 1] +=  2 * (k - v)
                bits[i] -= (k - v)
                ok = True
                break
            else:
                bits[i+1] += 2 * bits[i]
                v += bits[i]
                bits[i] = 0
    if ok:
        print('YES')
        res = []
        for i in range(m):
            for j in range(bits[i]):
                res.append(int(math.pow(2, m - i - 1)))
        print(' '.join(map(str, res)))
    else:
        print('NO')