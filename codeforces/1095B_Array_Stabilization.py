n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
if a[-1] - a[1] <= a[-2] - a[0]:
    print(a[-1] - a[1])
else:
    print(a[-2] - a[0])