n, m = list(map(int, input().strip().split()))
t, b, l, r = -1, -1, -1, -1
for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j] == 'B':
            if t == -1:
                t = i + 1
            if l == -1:
                l = j + 1
            r = j + 1
            b = i + 1
print((t + b) // 2, (l + r) // 2)