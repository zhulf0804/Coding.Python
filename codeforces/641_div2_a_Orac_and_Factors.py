import math
import sys

input = sys.stdin.readline

t = int(input())


def f(x):
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return x


for _ in range(t):
    n, k = list(map(int, input().split()))
    ans = n
    for i in range(k):
        if ans % 2 == 0:
            ans += (k - i) * 2
            break
        ans += f(n)
        n = ans
    print(ans)