import math


n = int(input())

def helper(n, k):
    summa, summb = 0, 0
    while n > 0:
        if n > k:
            summa += k
            n -= k
        else:
            summa += n
            break
        #cur = int(n*0.1)
        #cur = math.floor(n * 0.1)
        cur = n // 10
        summb += cur
        n -= cur
        #print(n)
    return summa, summb

#for k in range(1, n+1):
#    summa, summb = helper(n, k)
#    if summa >= summb:
#        print(k)
#        break
l, r = 1, n
while l < r:
    mid = (l + r) // 2
    summa, summb = helper(n, mid)
    #print(l, r, mid, summa, summb, n)
    if summa >= summb:
        r = mid
    else:
        l = mid + 1

print(l)