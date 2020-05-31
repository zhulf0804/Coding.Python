n = int(input())
x, y = list(map(int, input().split()))

a = max(x, y) - 1
b = max(n - x, n - y)

if a <= b:
    print("White")
else:
    print('Black')