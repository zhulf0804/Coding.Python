n = int(input())
a = list(map(int, input().split()))

c = 1
res = []
d = {}
v = {}
ok = True
for item in a:
    if d.get(item, 0) == 0:
        d[item] = n - item - 1
        v[item] = c
        c += 1
    else:
        d[item] -= 1
    res.append(v[item])

for k, v in d.items():
    if v != 0:
        ok = False
        break
if ok:
    print('Possible')
    print(' '.join(map(str, res)))
else:
    print('Impossible')