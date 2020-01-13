import heapq
N = int(input().strip())
V = list(map(int, input().strip().split()))
T = list(map(int, input().strip().split()))

res = []
pq = []
summ = 0
for i in range(N):
    cur = 0
    heapq.heappush(pq, summ + V[i])
    summ += T[i]
    while pq:
        item = pq[0]
        #print(item, type(item))
        if summ < item:
            cur += (len(pq) * T[i])
            break
        else:
            heapq.heappop(pq)
            cur += (item - (summ - T[i]))
    res.append(str(cur))
print(" ".join(res).strip())
'''
# PriorityQueue 超时
from queue import PriorityQueue

N = int(input().strip())
V = list(map(int, input().strip().split()))
T = list(map(int, input().strip().split()))

res = []
pq = PriorityQueue()
summ = 0
for i in range(N):
    cur = 0
    pq.put(summ + V[i])
    summ += T[i]
    while not pq.empty():
        item = pq.queue[0]
        #print(item, type(item))
        if summ < item:
            cur += (pq.qsize() * T[i])
            break
        else:
            pq.get()
            cur += (item - (summ - T[i]))
    res.append(str(cur))
print(" ".join(res).strip())
'''

'''
# 暴力解法
for i in range(N):
    cur = 0
    for j in range(i+1):
        cur += min(T[i], V[j])
        V[j] -= min(T[i], V[j])
    res.append(str(cur))
print(" ".join(res).strip())
'''

# 10 10 5
# 6 7 2

# q: 10, 10 + 6, 5 + 6 + 7
# 6, 4 + 7, 3 + 2