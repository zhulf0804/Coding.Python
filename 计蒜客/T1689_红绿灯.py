line = input()
n, m = int(line.strip().split()[0]), int(line.strip().split()[1])
line = input()
a = [int(item) for item in line.strip().split()]
line = input()
r = [int(item) for item in line.strip().split()]
line = input()
g = [int(item) for item in line.strip().split()]

#print(n, m)
#print(a)
#print(r)
#print(g)
t = [0] * n
a.insert(0, m)
res = []
last = 0
for i in range(n):
    cur = a[i] + last
    wait = 0
    loc = cur % (r[i] + g[i])
    #print(loc)
    if loc > g[i]:
        wait = g[i] + r[i] - loc
    last = cur + wait
    res.append(last)

for i in range(n):
    print(res[i])
