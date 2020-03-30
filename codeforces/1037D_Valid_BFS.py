import sys
input=sys.stdin.readline


n = int(input())
btree = [[] for _ in range(n+1)]
for i in range(n-1):
    x, y = list(map(int, input().split()))
    btree[x].append(y)
    btree[y].append(x)
#print(btree)
a = list(map(int, input().split()))

father = [-1] * (n + 1)
visited = [0] * (n + 1)
q = [1]
q_cur = 0
while q_cur < len(q):
    front = q[q_cur]
    q_cur += 1
    nodes = btree[front]
    for node in nodes:
        if not visited[node]:
            father[node] = front
            visited[node] = 1
            q.append(node)

q = [1]
q_cur = 0
cur = 1
visited = [0] * (n + 1)
visited[1] = 1

while q_cur < len(q):
    front = q[q_cur]
    q_cur += 1
    while cur < n and not visited[a[cur]] and father[a[cur]] == front:
        visited[a[cur]] = 1
        q.append(a[cur])
        cur += 1

ok = True
for i in range(1, n + 1):
    if not visited[i]:
        ok = False
        break
if ok:
    print("Yes")
else:
    print("No")

'''
# 上面的实现是list模拟队列
# 下面的是调用python的队列

from collections import deque
import sys
input=sys.stdin.readline


n = int(input())
btree = [[] for _ in range(n+1)]
for i in range(n-1):
    x, y = list(map(int, input().split()))
    btree[x].append(y)
    btree[y].append(x)
#print(btree)
a = list(map(int, input().split()))

father = [-1] * (n + 1)
visited = [0] * (n + 1)
q = deque()
q.append(1)
while len(q):
    front = q.popleft()
    nodes = btree[front]
    for node in nodes:
        if not visited[node]:
            father[node] = front
            visited[node] = 1
            q.append(node)

q = deque()
q.append(1)
cur = 1
visited = [0] * (n + 1)
visited[1] = 1

while len(q):
    front = q.popleft()
    while cur < n and not visited[a[cur]] and father[a[cur]] == front:
        visited[a[cur]] = 1
        q.append(a[cur])
        cur += 1

ok = True
for i in range(1, n + 1):
    if not visited[i]:
        ok = False
        break
if ok:
    print("Yes")
else:
    print("No")
'''