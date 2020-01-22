import heapq


def heap_sort(A):
    heap = []
    for item in A:
        heapq.heappush(heap, item)
    cur = 0
    while heap:
        A[cur] = heapq.heappop(heap)
        cur += 1


A = [2, 3, 4, 1]
heap_sort(A)
print(A)