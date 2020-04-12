from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        queue = []
        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)
        res = []
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return res if len(res) == numCourses else []

