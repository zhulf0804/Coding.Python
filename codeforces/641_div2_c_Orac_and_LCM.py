import math

n = int(input())
a = list(map(int, input().split()))

def helper(x, d):
    upper = math.floor(math.sqrt(x))
    for i in range(2, upper + 1):
        if x % i == 0:
            d[i] = d.get(i, 0) + 1
            if i * i != x:
                d[x // i] = d.get(x // i, 0) + 1
    d[x] = d.get(x, 0) + 1
    return d


def lcm(a, b):
    upper = min(a, b)
    for i in range(upper, 0, -1):
        if a % i == 0 and b % i == 0:
            return a * b // i


d = {}
for item in a:
    d = helper(item, d)
ans = 1
for k, v in d.items():
    if v >= n - 1:
        ans = lcm(ans, k)
print(ans)