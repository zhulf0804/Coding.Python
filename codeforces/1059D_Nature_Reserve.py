# 理解算法
# 估算最大半径
# 精度丢失问题
# 由于精度问题，控制循环次数
# 输出丢失精度问题
import math

n = int(input())
points = []
npt = 0
for i in range(n):
    point = list(map(int, input().split()))
    if point[1] < 0:
        npt += 1
        point[1] = -point[1]
    points.append(point)
if npt < n and npt > 0:
    print(-1)
else:
    l, r = 0, 1e16
    count = 100
    while abs(r - l) > 1e-6 and count > 0:
        count -= 1
        ok = True
        mid = (l + r) / 2
        a, b = -float('inf'), float('inf')
        for i in range(n):
            x, y = points[i]
            if y > 2 * mid:
                l = mid
                ok = False
                break
            delta = math.sqrt(y * (2*mid - y))
            # delta = math.sqrt(math.pow(mid, 2) - math.pow(mid-y, 2)) # 数据精度丢失
            a, b = max(a, x - delta), min(b, x + delta)
            #print("x: {}, y: {}, a: {}, b: {}, delta: {}".format(x, y, a, b, delta))
        if not ok:
            continue
        #print(a, b, l, r, mid, abs(r - l))
        if a > b:
            l = mid
        else:
            r = mid
    print((l + r) / 2)
