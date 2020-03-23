n = int(input())
ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

'''
visited = [[0] * (n + 1) for _ in range(n + 1)]


def helper(cur_x, cur_y):
    #print(visited)
    if cur_x <= 0 or cur_x > n:
        return False
    if cur_y <= 0 or cur_y > n:
        return False
    if visited[cur_x][cur_y]:
        return False
    visited[cur_x][cur_y] = 1
    if cur_x == cx and cur_y == cy:
        return True

    if cur_y == ay or cur_x == ax or abs(cur_x - ax) == abs(cur_y - ay):
        return False

    return helper(cur_x - 1, cur_y - 1) \
           or helper(cur_x - 1, cur_y) \
           or helper(cur_x - 1, cur_y + 1) \
           or helper(cur_x, cur_y - 1) \
           or helper(cur_x, cur_y + 1) \
           or helper(cur_x + 1, cur_y-1) \
           or helper(cur_x + 1, cur_y) \
           or helper(cur_x + 1, cur_y+1)


if (ax - bx) * (ax - cx) <= 0 or (ay - by) * (ay - cy) <= 0:
    print("NO")
else:
    if helper(bx, by):
        print("YES")
    else:
        print("NO")
'''

if (ax - bx) * (ax - cx) <= 0 or (ay - by) * (ay - cy) <= 0:
    print("NO")
else:
    print("YES")