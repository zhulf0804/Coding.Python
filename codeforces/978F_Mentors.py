from collections import defaultdict

n, k = list(map(int, input().strip().split()))
r = list(map(int, input().strip().split()))
r_l = []
for i in range(1, n+1):
    r_l.append([i, r[i-1]])

r_l.sort(key=lambda x: x[1])

d = {}
c = []
for i in range(k):
    x, y = list(map(int, input().strip().split()))
    if r[x-1] < r[y-1]:
        d[y] = d.get(y, 0) + 1
    elif r[x - 1] > r[y-1]:
        d[x] = d.get(x, 0) + 1

count = {}
for i in range(n):
    j, val = r_l[i]
    tmp = i
    if val in count:
        tmp = count[val]
    else:
        count[val] = i
    cur = max(0, tmp - d.get(j, 0))
    r_l[i].append(cur)
r_l.sort(key=lambda x: x[0])

#print(r_l)

res = []
for i in range(len(r_l)):
    res.append(str(r_l[i][2]))
print(" ".join(res))