import math


n, m, d = list(map(int, input().split()))
features = []
for i in range(n):
    feature = list(map(float, input().split()))
    features.append(feature)


def dist(a, b):
    dist = 0
    for i in range(len(a)):
        cur = math.pow(a[i]-b[i], 2)
        dist += cur
    return math.sqrt(dist)


def find(p, uf):
    if uf[p] < 0:
        return p
    uf[p] = find(uf[p], uf)
    return uf[p]


def union(p, q, uf):
    proot = find(p, uf)
    qroot = find(q, uf)
    if proot == qroot:
        return
    elif uf[proot] > uf[qroot]:
        uf[qroot] += uf[proot]
        uf[proot] = qroot
    else:
        uf[proot] += uf[qroot]
        uf[qroot] = proot


if m == 1:
    res = list(map(str, list(range(1, n + 1))))
    print(' '.join(res))
elif m == n:
    res = list(map(str, [1]*n))
    print(' '.join(res))
else:
    d = {}
    for i in range(n):
        for j in range(i+1, n):
            cur = dist(features[i], features[j])
            d['{}_{}'.format(i, j)] = cur
    d = sorted(d.items(), key=lambda x: x[1])
    #print(d)
    thresh = float('inf')
    uf = [-1] * n
    for i in range(len(d)):
        #print(i)
        x_y, dst = d[i]
        x, y = list(map(int, x_y.split('_')))
        uf_x = find(x, uf)
        uf_y = find(y, uf)
        if uf_x == uf_y:
            continue
        if dst >= thresh:
            break
        if uf[uf_x] + m == 0 or uf[uf_y] + m == 0:
            #thresh = min(dst, thresh)
            #continue
            break
        if abs(uf[uf_x] + uf[uf_y]) <= m:
            union(uf_x, uf_y, uf)
        else:
            thresh = dst

    #print(uf)
    res = []
    cur = 1
    dd = {}
    for i in range(n):
        uf_i = find(i, uf)
        if uf_i in dd:
            res.append(dd[uf_i])
        else:
            dd[uf_i] = cur
            res.append(cur)
            cur += 1

    res = list(map(str, res))
    print(' '.join(res))