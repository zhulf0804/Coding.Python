n = int(input())
xs = list(map(int, input().strip().split()))
ys = list(map(int, input().strip().split()))

ok = True
cur = 0
for i in range(n):
    cur += (xs[i] - ys[i])

if cur >= 0:
    print("Yes")
else:
    print("No")