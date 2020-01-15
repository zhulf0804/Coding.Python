n, m = list(map(int, input().strip().split(' ')))
d = {}
visited = {}
ok = True
for i in range(n):
    line = input().strip()
    if line not in d:
        d[line] = 1
        for j in range(m):
            if line[j] == '#':
                if j in visited:
                    ok = False
                    break
                else:
                    visited[j] = 1
if ok:
    print("Yes")
else:
    print("No")