# (n + 1) * (x - 1) + y
class Solution:
    def leastInterval(self, tasks, n):
        d = {}
        for task in tasks:
            d[task] = d.get(task, 0) + 1
        vs = sorted(d.values())
        x = vs[-1]
        y = 1
        for i in range(len(vs) - 2, -1, -1):
            if vs[i] == x:
                y += 1
            else:
                break
        
        ans = (n + 1) * (x - 1) + y 
        return max(ans, len(tasks))
        