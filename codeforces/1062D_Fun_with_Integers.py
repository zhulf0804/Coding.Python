n = int(input())

ans = 0
for i in range(2, n + 1):
    cur = n // i
    if cur == 1:
        continue
    summ = (cur + 2) * (cur - 1) // 2
    ans += summ

print(ans * 4)