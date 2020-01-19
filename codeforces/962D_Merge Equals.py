import heapq


n = int(input())
nums = list(map(int, input().strip().split()))


pq = []
for i, item in enumerate(nums):
    heapq.heappush(pq, (item, i))

res = []
while len(pq) >= 2:
    x = pq[0]
    heapq.heappop(pq)
    y = pq[0]
    #print(x, y)
    if x[0] == y[0]:
        heapq.heappush(pq, (2 * y[0], y[1]))
        heapq.heappop(pq)
    else:
        res.append(x)
res.append(pq[0])

res = sorted(res, key=lambda x: x[1])
ans = []
for k, v in res:
    ans.append(str(k))
print(len(ans))
print(' '.join(ans))