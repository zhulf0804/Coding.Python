import math

n = int(input())
upper = math.floor(math.sqrt(n)) + 1
ans = float('inf')
for i in range(1, upper):
    cur = i
    cur += (n // i)
    if n % i != 0:
        cur += 1
    ans = min(ans, cur)
print(ans)