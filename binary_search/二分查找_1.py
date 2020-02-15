# https://nanti.jisuanke.com/t/T1560
import sys
input=sys.stdin.readline

n, m = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
a.sort()


def find(x):
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False


for i in range(m):
    x = int(input())
    flag = find(x)
    if flag:
        print("YES")
    else:
        print("NO")