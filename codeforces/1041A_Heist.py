n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

print(a[-1] - a[0] + 1 - n)