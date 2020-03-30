import math


a, b, x, y = list(map(int, input().split()))


def gcd(m, n):
    if n == 0:
        return m
    if n == 1:
        return n
    remainder = m % n
    return gcd(n, remainder)

gcd_v = gcd(x, y)
#print(gcd_v)
x = x // gcd_v
y = y // gcd_v
m = a // x
n = b // y
res = min(m, n)

print(res)