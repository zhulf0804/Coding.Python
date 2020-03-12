n = int(input())
p = list(map(int, input().strip().split()))

res = []
for i in range(n):
    d = {}
    cur = i + 1
    while cur not in d:
        d[cur] = 1
        cur = p[cur - 1]
    res.append(str(cur))

print(" ".join(res))