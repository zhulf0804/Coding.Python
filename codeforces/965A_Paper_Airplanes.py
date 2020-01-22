k, n, s, p = list(map(int, input().strip().split()))

total = k * n

mmin = 1
while mmin * p // k * s < n:
    mmin += 1
print(mmin)