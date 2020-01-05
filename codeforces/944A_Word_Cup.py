import math


line = input()
n, a, b = list(map(int, line.strip().split()))
total = int(math.log2(n))

#print(n, a, b)
if a > b:
    a, b = b, a
l, r = 1, n
count = 0
while True:
    mid = (l + r) // 2
    if a <= mid and b > mid:
        break
    if a > mid:
        l = mid + 1
    elif b <= mid:
        r = mid
    count += 1

if count == 0:
    print("Final!")
else:
    print(total - count)

