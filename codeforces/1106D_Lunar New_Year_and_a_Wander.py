import heapq

n, m = list(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    edges[a].append(b)
    edges[b].append(a)

heap = []
visited, res = [0] * (n+1), []
heapq.heappush(heap, 1)
visited[1] = 1
while len(heap) > 0:
    cur = heapq.heappop(heap)
    res.append(cur)
    for adj in edges[cur]:
        if not visited[adj]:
            heapq.heappush(heap, adj)
            visited[adj] = 1

print(' '.join(map(str, res)))