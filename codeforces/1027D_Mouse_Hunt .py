n = int(input())
c = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
resd = {}
res = 0
tmpd = {}
for i in range(n):
    cur = i + 1
    d = {}
    group = []
    flag = False
    while cur not in d:
        if cur in tmpd:
            flag = True
            break
        d[cur] = 1
        tmpd[cur] = 1
        group.append(cur)
        cur = a[cur - 1]
    if flag:
        continue
    mmin = float('inf')
    ind = float('inf')
    flag = False
    for item in group:
        if item == cur:
            flag = True
        if flag:
            mmin = min(c[item - 1], mmin)
            ind = min(ind, item)
    if ind in resd:
        continue
    else:
        resd[ind] = 1
        res += mmin

print(res)