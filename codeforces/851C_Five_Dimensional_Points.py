n = int(input())

points = []
for i in range(n):
    pt = list(map(int, input().split()))
    points.append(pt)

flag = [1] * n
for i in range(n):
    a = points[i]
    ok = False
    for j in range(n):
        if ok:
            break
        if j == i:
            continue
        b = points[j]
        for k in range(n):
            if k == i or k == j:
                continue
            c = points[k]
            summ = 0
            for z in range(5):
                u = b[z] - a[z]
                v = c[z] - a[z]
                summ += u*v
            if summ > 0:
                flag[i] = 0
                ok = True
                break

res = []
for i in range(n):
    if flag[i]:
        res.append(i + 1)

print(len(res))
for i in range(len(res)):
    print(res[i])