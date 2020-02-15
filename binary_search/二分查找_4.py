# https://nanti.jisuanke.com/t/T1563

import sys
input=sys.stdin.readline


n, m = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
a.sort()


def find_left(x):
    # 第一个大于等于 x 的索引
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid

    if a[l] < x:
        return l + 1
    else:
        return l


def find_right(x):
    # 第一个大于 x 的索引
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid] <= x:
            l = mid + 1
        else:
            r = mid

    if a[l] <= x:
        return l + 1
    else:
        return l


for i in range(m):
    x = int(input())
    left = find_left(x)
    right = find_right(x)
    print(right - left)