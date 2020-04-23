import math


ax, ay, bx, by, cx, cy = list(map(int, input().split()))

ba = [ax - bx, ay - by]
bc = [cx - bx, cy - by]

ba_mul_bc = (ba[0] * bc[0] + ba[1] * bc[1]) ** 2
ba_dist = ba[0] ** 2 + ba[1] ** 2
bc_dist = bc[0] ** 2 + bc[1] ** 2

dist_ab = (ax - bx) ** 2 + (ay - by) ** 2
dist_bc = (bx - cx) ** 2 + (by - cy) ** 2
#print(ba_mul_bc, ba_dist, bc_dist)
if dist_ab == dist_bc and ba_mul_bc != ba_dist*bc_dist and ba_mul_bc + ba_dist*bc_dist != 0:
    print("Yes")
else:
    print("No")