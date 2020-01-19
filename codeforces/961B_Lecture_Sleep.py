n, k = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
t = list(map(int, input().strip().split()))

summ = 0
count = []
cur = 0
for i in range(n):
    if t[i] == 1:
        summ += a[i]
    else:
        cur += a[i]
    count.append(cur)
mmax = 0
for i in range(n):
    if i + k - 1 >= n:
        continue
    cur = count[i+k-1] - count[i]
    if t[i] == 0:
        cur += a[i]
    mmax = max(cur, mmax)

print(mmax + summ)

