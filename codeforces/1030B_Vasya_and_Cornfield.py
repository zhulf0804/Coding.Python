import math
n, d = list(map(int, input().split()))
m = int(input())

'''
def dist(pt, line):
    x, y = pt
    a, b, c = line
    return abs(a*x + b*y + c) / math.sqrt(a * a + b * b)
def helper(pt, line1, line2):
    dist1 = dist(pt, line1)
    dist2 = dist(pt, line2)
'''


for i in range(m):
    x, y = list(map(int, input().split()))
    a = x + y
    b = x - y
    if (a - d) * (2 * n - d - a) >= 0 and (b - d) * (-d - b) >= 0:
        print("YES")
    else:
        print("NO")
