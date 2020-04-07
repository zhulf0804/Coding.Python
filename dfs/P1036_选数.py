# https://www.luogu.com.cn/problem/P1036

import math

n, k = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0


def is_prime(y):
    if y == 0 or y == 1:
        return False
    if y == 2 or y == 3:
        return True
    up = math.floor(math.sqrt(y)) + 1
    ok = True
    for i in range(2, up + 1):
        if y % i == 0:
            return False
    return ok


def dfs(x, sum, z):
    global ans
    if z == k:
        if is_prime(sum):
            ans += 1
        return
    if x >= n:
        return
    dfs(x + 1, sum, z)
    dfs(x + 1, sum + b[x], z + 1)
dfs(0, 0, 0)
print(ans)