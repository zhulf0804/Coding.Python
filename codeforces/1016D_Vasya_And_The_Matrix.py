n, m = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
#print(n, m, a, b)
res = []
for i in range(n-1):
    cur = []
    if a[i] % 2 == 0:
        tmp = a[i] + 1
    else:
        tmp = a[i] - 1
    cur.append('1')
    l = m - 2
    for j in range(2, 2 + l):
        cur.append('0')
    cur.append(str(tmp))
    res.append(cur)
    #print(cur)
last = []
for i in range(m):
    cur = b[i]
    for j in range(n-1):
        cur ^= int(res[j][i])
    last.append(str(cur))
#print(last)
val = 0
for i in range(m):
    val ^= int(last[i])
#print(val, a[n-1])
if val == a[n-1]:
    print("YES")
    for i in range(n-1):
        print(" ".join(res[i]))
    print(" ".join(last))
else:
    print("NO")