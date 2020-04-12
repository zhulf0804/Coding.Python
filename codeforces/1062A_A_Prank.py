n = int(input())
a = list(map(int, input().split()))
s, e = 0, 1
mmax = 0
while e < n:
    while e < n and a[e] == a[e-1] + 1:
        e += 1
    cur = e - s - 2
    #print(s, e)
    if a[e-1] == 1000 or a[s] == 1:
        cur += 1
    mmax = max(mmax, cur)
    s, e = e, e + 1

print(mmax)