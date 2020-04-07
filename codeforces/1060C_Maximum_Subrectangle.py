n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = int(input())

rows = [float('inf')] * (n + 1)
cols = [float('inf')] * (m + 1)
for i in range(n):
    summ = 0
    for j in range(i, n):
        summ += a[j]
        l = j - i  + 1
        rows[l] = min(rows[l], summ)

for i in range(m):
    summ = 0
    for j in range(i, m):
        summ += b[j]
        l = j - i + 1
        cols[l] = min(cols[l], summ)

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cur = rows[i] * cols[j]
        if cur <= x:
            ans = max(ans, i * j)
print(ans)