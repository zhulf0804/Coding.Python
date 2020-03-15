n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

d = {}
for i in range(n):
    l = len(str(a[i]))
    y = a[i] % k
    d[(l, y)] = d.get((l, y), 0) + 1

res = 0
for i in range(n):
    for j in range(1, 11):
        cur = a[i] * int(pow(10, j))
        cur_l = len(str(a[i]))
        cur_y = a[i] % k
        y = cur % k
        if (j, (k - y) % k) in d:
            #print(a[i], cur, j, d[(j, (k-y)%k)])
            res += d[(j, (k-y)%k)]
            if (cur_l, cur_y) == (j, (k-y)%k):
                res -= 1
print(res)