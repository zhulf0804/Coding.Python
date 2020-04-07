n, m = list(map(int, input().split()))
maps, visited = [], []

for i in range(n):
    cur = input().strip()
    maps.append(cur)
    #visited.append(cur)
    map_cur = [1 if item == '#' else 0 for item in cur]
    visited.append(map_cur)
#print(visited)
for i in range(1, n-1):
    for j in range(1, m-1):
        cur = 0
        for u in range(-1, 2):
            for v in range(-1, 2):
                if u == 0 and v == 0:
                    continue
                if maps[i + u][j + v] == '#':
                    cur += 1
        if cur < 8:
            continue
        for u in range(-1, 2):
            for v in range(-1, 2):
                if u == 0 and v == 0:
                    continue
                visited[i + u][j + v] = 0
        #print(visited)

#print(visited)
can = True
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            can = False
            break
if can:
    print("YES")
else:
    print("NO")