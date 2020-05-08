n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = {}
for i, item in enumerate(a):
    d[item] = i + 1


res = []
cur = 1
for i in range(n):
    z = d[b[i]]
    if z < cur:
        res.append(0)
    else:
        res.append(z - cur + 1)
        cur = z + 1

print(' '.join(map(str, res)))