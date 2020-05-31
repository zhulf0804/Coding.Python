import math


def helper(x):
    up = math.floor(math.sqrt(x))
    i = 2
    while i <= up:
        if x % i == 0:
            return i
        i += 1
    return x


n = int(input())
if n // 2 == 0:
    print(n // 2)
else:
    print(1 + (n - helper(n)) // 2)