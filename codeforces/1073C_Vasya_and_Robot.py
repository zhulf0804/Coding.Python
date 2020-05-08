n = int(input())
root = input()
x, y = list(map(int, input().split()))

curx, cury = 0, 0
dx, dy = [0], [0]
for i in range(n):
    if root[i] == 'L':
        curx -= 1
    if root[i] == 'R':
        curx += 1
    if root[i] == 'U':
        cury += 1
    if root[i] == 'D':
        cury -= 1
    dx.append(curx)
    dy.append(cury)

if curx == x and cury == y:
    print(0)
else:
    ans = n + 1
    for i in range(1, n+1):
        l, r = i, n
        while l <= r:
            mid = (l + r) // 2
            dx1 = dx[i - 1]
            dy1 = dy[i - 1]
            dx2 = dx[n] - dx[mid]
            dy2 = dy[n] - dy[mid]
            ddx = x - (dx1 + dx2)
            ddy = y - (dy1 + dy2)
            z = mid - i + 1 - abs(ddx) - abs(ddy)
            if z >= 0 and z % 2 == 0:
                ans = min(ans, mid - i + 1)
                r = mid - 1
            else:
                l = mid + 1

    if ans == n + 1:
        print(-1)
    else:
        print(ans)