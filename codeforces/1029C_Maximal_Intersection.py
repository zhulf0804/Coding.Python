import sys
input=sys.stdin.readline

n = int(input())
pts = []
for i in range(n):
    l, r = list(map(int, input().split()))
    pts.append([l, r])

pts = sorted(pts, key=lambda x: x[1])

mmax = pts[1][0]
for pt in pts[1:]:
    l, r = pt
    mmax = max(mmax, l)

res1 = pts[1][1] - mmax if pts[1][1] - mmax >= 0 else 0

r = pts[0][1]
l = pts[0][0]
pts = sorted(pts[1:], key=lambda x: x[0])
if len(pts) > 1:
    l = max(l, pts[-2][0])

res2 = r - l if r - l >= 0 else 0

print(max(res1, res2))