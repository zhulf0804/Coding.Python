import math


A, B = list(map(int, input().split()))

a = []
b = []

cur = 0
while cur * (cur + 1) <= 2 * (A + B):
    cur += 1

cur -= 1

for i in range(cur, 0, -1):
    if i <= A:
        a.append(str(i))
        A -= i
    elif i <= B:
        b.append(str(i))
        B -= i

print(len(a))
print(' '.join(a))
print(len(b))
print(' '.join(b))
