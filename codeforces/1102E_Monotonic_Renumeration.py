n = int(input())
a = list(map(int, input().split()))

first, last = {}, {}
for i in range(n):
    if a[i] not in first:
        first[a[i]] = i
    last[a[i]] = i

vs = list(set(a))
lrs = []
for v in vs:
    l, r = first[v], last[v]
    lrs.append([l, r])

lrs = sorted(lrs, key=lambda x:x[0])
ans = 1
fr = lrs[0][1]
for l, r in lrs[1:]:
    if l > fr:
        ans = ans * 2 ** (l - fr)
        ans = ans % 998244353
    fr = max(r, fr)

print(ans)