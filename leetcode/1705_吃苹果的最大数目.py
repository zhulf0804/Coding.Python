from typing import List
import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap, ans, i = [], 0, 0
        while i < len(apples) or len(heap) > 0:
            if i < len(apples):
                apple, day = apples[i], days[i]
                if apple != 0:
                    heapq.heappush(heap, [day + i, apple])
            while len(heap) > 0 and (heap[0][0] <= i or heap[0][1] <= 0):
                heapq.heappop(heap)
            if len(heap) > 0:
                ans += 1
                heap[0][1] -= 1
            i += 1
        return ans

a = Solution()
apples = [3,0,0,0,0,2] #[1,2,3,5,2]
days = [3,0,0,0,0,2] #[3,2,1,4,2]
print(a.eatenApples(apples, days))