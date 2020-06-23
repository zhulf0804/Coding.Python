n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

b = sorted(list(set(a)))
if b[0] == 0:
    b = b[1:]
res = []
pre = 0
for item in b:
    res.append(item - pre)
    pre = item

if len(res) >= k:
    for item in res[:k]:
        print(item)
else:
    for item in res:
        print(item)
    for i in range(k - len(res)):
        print(0)