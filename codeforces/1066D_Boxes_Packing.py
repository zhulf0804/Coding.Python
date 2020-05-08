n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))

summ = []
cur = 0
for item in a[::-1]:
    cur += item
    summ.append(cur)

def helper(x, summ, l, r):
    while l < r:
        mid = l + (r - l + 1) // 2
        if summ[mid] > x:
            r = mid - 1
        else:
            l = mid
    if summ[l] <= x:
        return l
    else:
        return l - 1
res = []
l = 0
z = k
while len(res) < m and l < n:
    #print(l, n - 1)
    x = helper(z, summ, l, n - 1)
    res.append(x)
    z = summ[x] + k
    l = x + 1
#print(res)
print(res[-1] + 1)