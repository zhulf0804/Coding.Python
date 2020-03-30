# https://nanti.jisuanke.com/t/T1211
W, H = list(map(int, input().split()))
maps = []
sx, sy = 0, 0
for i in range(H):
    line = input()
    maps.append(line)
    if '@' in line:
        sy = i
        sx = line.index('@')

visited = [[0] * W for _ in range(H)]

def helper(x, y, visited):
    if x < 0 or x >= W or y < 0 or y >= H:
        return 0
    if maps[y][x] == '#' or visited[y][x]:
        return 0
    count = 1
    visited[y][x] = 1
    count += helper(x + 1, y, visited)
    count += helper(x - 1, y, visited)
    count += helper(x, y + 1, visited)
    count += helper(x, y - 1, visited)
    return count

print(helper(sx, sy, visited))