n, m = list(map(int, input().split()))

a = ['1'] * n
b = ['8'] * (n - 1) + ['9']
print(''.join(a))
print(''.join(b))