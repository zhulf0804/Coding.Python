T = int(input())
for _ in range(T):
    n = int(input())
    snts = []
    for i in range(n):
        l, r = list(map(int, input().split()))
        snts.append([l, r, i])
    snts = sorted(snts, key=lambda x: x[0])
    res, ok = [1], T
    rs, v, ids = [snts[0][1], -1], 0, [snts[0][2]]
    for i in range(1, n):
        l, r, id = snts[i]
        ids.append(id)
        if l <= rs[v]:
            res.append(v+1)
            rs[v] = max(rs[v], r)
        else:
            v += 1
            v = v % 2
            res.append(v+1)
            rs[v] = r
    if len(set(res)) == 1:
        print('-1')
    else:
        res = sorted(zip(ids, res), key=lambda x:x[0])
        res = [item[1] for item in res]
        print(' '.join(map(str, res)))