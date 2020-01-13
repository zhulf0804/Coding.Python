n, m = list(map(int, input().strip().split()))
xs = list(map(int, input().strip().split()))
ys = list(map(int, input().strip().split()))

sumx = []
cur = 0
for i in range(n):
    cur += xs[i]
    sumx.append(cur)

#sumy = []
cur = 0
res = 0
i = 0
for j in range(m):
    cur += ys[j]
    #sumy.append(cur)
    while cur > sumx[i]:
        i += 1
    if cur == sumx[i]:
        res += 1
        i += 1
print(res)

'''
res = 0
d = []
for item in sumx:
    if item in sumy:
        #j = sumy.index(item)
        #d[i] = j
        res += 1
print(res)
'''