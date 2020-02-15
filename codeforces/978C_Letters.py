n, m = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

summ = []
cur = 0
for item in a:
    cur += item
    summ.append(cur)

def find(x):
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if summ[mid] < x:
            l = mid + 1
        else:
            r = mid
    f = l + 1
    if l == 0:
        k = x
    else:
        k = x - summ[l-1]
    return f, k


for num in b:
    f, k = find(num)
    print(f, k)