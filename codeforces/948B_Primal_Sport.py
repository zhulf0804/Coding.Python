import math


def max_prime_factor(n):
    cur = 2
    while n != 1:
        while n % cur == 0:
            n = n // cur
        if n == 1:
            break
        cur += 1
        if cur > math.sqrt(n):
            return n
    return cur

# 78962

X2 = int(input().strip())
p1 = max_prime_factor(X2)
#print(X2, p1)
res = float('inf')
for X1 in range(X2 - p1 + 1, X2 + 1):
    if p1 >= X1:
        continue
    p2 = max_prime_factor(X1)
    #print(X1, p2)
    if X1 - p2 + 1 > p2:
        res = min(res, X1 - p2 + 1)
print(res)