def lowbit(index):
    return index & (-index)


def update(index, delta=1):
    while index <= size:
        tree[index] += delta
        index += lowbit(index)



def query(index):
    res = 0
    while index > 0:
        res += tree[index]
        index -= lowbit(index)
    return res


n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
#n, t = 5, 4
#a = [5, -1, 3, 4, -1]

summ_raw = [0]
summ_minus = []
cur = 0
for i in range(n):
    cur += a[i]
    summ_raw.append(cur)
    summ_minus.append(cur - t)

summ = sorted(list(set(summ_raw + summ_minus)))
size = len(summ)
d = {}
for i in range(size):
    d[summ[i]] = i + 1
#print(summ)
#print(d)
tree = [0] * (size + 1)
update(d[0])

res = 0
for i in range(1, n+1):
    v = summ_raw[i]
    index = d[v - t]
    cur = (query(size) - query(index))
    #print(tree, size, query(size), cur, v, index)
    res += cur
    update(d[v])
print(res)