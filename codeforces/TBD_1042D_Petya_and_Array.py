# 此算法超时
n, t = list(map(int, input().split()))
a = list(map(int, input().split()))

summ = []
cur = 0
for i in range(n):
    cur += a[i]
    summ.append(cur)

res = 0
for i in range(n):
    for j in range(i, n):
        cur_summ = summ[j] - summ[i] + a[i]
        if cur_summ < t:
            res += 1

print(res)