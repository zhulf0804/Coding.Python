n, m = list(map(int, input().strip().split()))
visited = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]
#print(edges)
#
for i in range(m):
    x, y = list(map(int, input().strip().split()))
    edges[x].append(y)
    edges[y].append(x)

res = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    visited[i] = 1
    if len(edges[i]) <= 1 or len(edges[i]) > 2:
        continue
    next = edges[i][0]
    cur = i
    while next != i and not visited[next]:
        visited[next] = 1
        if len(edges[next]) <= 1 or len(edges[next]) > 2:
            visited[next] = 1
            break
        if edges[next][0] == cur:
            cur = next
            next = edges[next][1]
        else:
            cur = next
            next = edges[next][0]


    if next == i:
        res += 1

print(res)