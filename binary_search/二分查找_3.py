# https://nanti.jisuanke.com/t/T1562

import sys
input=sys.stdin.readline


n, m = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
a.sort()


def find(x):
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid] <= x:
            l = mid + 1
        else:
            r = mid

    if a[l] <= x:
        return -1
    else:
        return a[l]


for i in range(m):
    x = int(input())
    res = find(x)
    print(res)