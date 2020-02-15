# https://nanti.jisuanke.com/t/T1556

import sys
input=sys.stdin.readline


n, m = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
a.sort()


def find(x):
    l, r = 0, n - 1
    while l < r - 1:
        mid = (l + r) // 2
        if a[mid] < x:
            l = mid
        else:
            r = mid - 1

    if l == r:
        if a[l] < x:
            return a[l]
        else:
            return -1
    elif l == r - 1:
        if a[l] >= x:
            return -1
        elif a[r] < x:
            return a[r]
        else:
            return a[l]


for i in range(m):
    x = int(input())
    res = find(x)
    print(res)