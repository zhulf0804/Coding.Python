# https://www.luogu.com.cn/problem/P1443

dxy = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

n, m, x, y = list(map(int, input().split()))
visited = [-1] * (n * m)
visited[(x - 1) * m + (y - 1)] = 0
q = [(x - 1) * m + (y - 1)]
ind = 0

def check(a, b):
    if a < 0 or a >= n or b < 0 or b >= m:
        return False
    return True

while ind < len(q):
    v = q[ind]
    x, y = v // m, v % m
    ind += 1
    for dx, dy in dxy:
        a, b = x + dx, y + dy
        if not check(a, b):
            continue
        if visited[a * m + b] >= 0:
            continue
        visited[a * m + b] = visited[v] + 1
        q.append(a * m + b)

for i in range(n):
    line = visited[i * m : (i + 1) * m]
    #print('     '.join(map(str, line)))
    res = ''
    for j in range(m):
        res += '%(v)-5s'%{'v':str(line[j])}
    print(res)