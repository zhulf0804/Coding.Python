n, k = list(map(int, input().strip().split()))
values = list(map(int, input().strip().split()))
d = {}
res = []
for i in range(n):
    if values[i] not in d:
        res.append(str(i+1))
        d[values[i]] = 1
if len(res) < k:
    print("NO")
else:
    print("YES")
    print(' '.join(res[:k]))