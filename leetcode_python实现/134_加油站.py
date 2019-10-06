from typing import List
class Solution_1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            cur = gas[i]
            cur_ind = i % len(gas)
            while cur >= cost[cur_ind]:
                next_ind = (cur_ind + 1) % len(gas)
                if next_ind == i:
                    return i
                cur = cur - cost[cur_ind] + gas[next_ind]
                cur_ind = next_ind
        return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas):
            cur = gas[i]
            cur_ind = i
            while cur >= cost[cur_ind]:
                next_ind = (cur_ind + 1) % len(gas)
                if next_ind == i:
                    return i
                cur = cur - cost[cur_ind] + gas[next_ind]
                cur_ind = next_ind
            if cur_ind + 1 <= i:
                break
            i = cur_ind + 1
        return -1


gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

s = Solution()
print(s.canCompleteCircuit(gas, cost))