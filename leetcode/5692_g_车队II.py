from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        res = [-1] * n
        queue, s_i = [-1] * n, 0
        for i in range(n-2, -1, -1):
            pos, speed = cars[i]
            while s_i >= 0:
                p, s = cars[queue[s_i]]
                if speed <= s:
                    s_i -= 1
                else:
                    if res[queue[s_i]] == -1:
                        t = (p - pos) / (speed - s)
                        res[i] = t
                        break
                    else:
                        if pos + speed * res[queue[s_i]] >= p + s * res[queue[s_i]]:
                            t = (p - pos) / (speed - s)
                            res[i] = t
                            break
                        else:
                            s_i -= 1
            if s_i < 0:
                res[i] = -1
            s_i += 1
            queue[s_i] = i
        return res

cars = [[1,2],[2,1],[4,3],[7,2]]
s = Solution()
print(s.getCollisionTimes(cars))