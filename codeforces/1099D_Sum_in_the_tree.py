from collections import defaultdict

n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

clds, pars = defaultdict(list), [0] * (n+1)
for i in range(n-1):
    cur, par = i + 2, p[i]
    clds[p[i]].append(cur)
    pars[cur] = par

ans, ok = s[0], True
i, q = 0, [1]
while i < len(q):
    cur = q[i]
    i += 1
    par_v = s[pars[cur] - 1]
    if cur in clds:
        mmin, summ, k = float('inf'), 0, 0
        for item in clds[cur]:
            mmin = min(mmin, s[item-1])
            summ += s[item-1]
            k += 1
            q.append(item)
        if s[cur - 1] != -1:
            continue
        if mmin < par_v:
            ok = False
            break
        ans -= par_v
        ans += (summ - (k-1)*mmin)
if ok:
    print(ans)
else:
    print(-1)