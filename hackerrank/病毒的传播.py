# https://www.hackerrank.com/contests/2020-deepglint/challenges/challenge-2390

import copy
from collections import deque

N, M = list(map(int, input().split()))
edges = [[] for _ in range(N+1)]
for i in range(M):
    x, y = list(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)

visited = [0] * (N + 1)


def bfs(i, visited):
    q = deque()
    q.append(i)
    cur = i
    visited[i] = 1
    cur_len = [0] * (N + 1)
    cur_len[i] = 1
    while len(q) > 0:
        cur = q.popleft()
        for item in edges[cur]:
            if not visited[item]:
                q.append(item)
                cur_len[item] = cur_len[cur] + 1
                visited[item] = 1
    return cur, cur_len[cur]


count = 0
mmin, mmax = 0, 0
for i in range(1, N+1):
    if not visited[i]:
        count += 1
        visited_cp = copy.copy(visited)
        cur, _ = bfs(i, visited)
        _, max_len = bfs(cur, visited_cp)
        mmin = max(max_len // 2, mmin)
        mmax = max(max_len, mmax)

print(count)
print(mmin, mmax-1)