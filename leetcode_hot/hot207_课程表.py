class Solution:
    def canFinish(self, numCourses, prerequisites):
        if len(prerequisites) == 0:
            return True

        graph = {node:[] for node in range(numCourses)}
        in_degree = {node:0 for node in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] = in_degree[a] + 1

        stack = []
        for node in range(numCourses):
            if in_degree[node] == 0:
                stack.append(node)
        
        ans = 0
        while stack:
            ans += 1
            a = stack.pop()
            for b in graph[a]:
                in_degree[b] -= 1
                if in_degree[b] == 0:
                    stack.append(b)
                    
        return ans >= numCourses
            