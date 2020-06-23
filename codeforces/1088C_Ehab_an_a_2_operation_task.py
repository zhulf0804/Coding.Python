n = int(input())
a = list(map(int, input().split()))

ans, res = 0, []
flag = False
summ = 0
for i in range(n-1, -1, -1):
    a[i] += summ
    cur = a[i] % (n + 1)
    if  cur == i + 1:
        continue
    delta = i + 1 + (n + 1 - cur)
    if cur < i + 1:
        delta = i + 1 - cur
    summ += delta
    item = '{} {} {}'.format(1, i + 1, delta)
    ans += 1
    res.append(item)
    if a[i] + delta >= n:
        flag = True
if flag:
    ans += 1
    res.append('{} {} {}'.format(2, n, n + 1))
print(ans)
if ans > 0:
    for j in range(ans):
        print(res[j])