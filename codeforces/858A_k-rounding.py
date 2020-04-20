import math

n, k = list(map(int, input().split()))
tmp = n
z = 0
while n % 10 == 0:
    n = n // 10
    z += 1
k = k - z

if k <= 0:
    print(tmp)
else:
    last = n % 10
    v = int(math.pow(10, k))
    if last == 5:
        i = 2
        cur = n
        while cur % v != 0:
            cur = n * i
            i += 2
        print(int(cur * math.pow(10, z)))
    elif last % 2 == 1:
        print(tmp * v)
    else:
        i = 5
        cur = n
        while cur % v != 0:
            cur = n * i
            i += 5
        print(int(cur * math.pow(10, z)))