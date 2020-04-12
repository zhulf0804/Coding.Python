import math

n = int(input())

factors, mmax, mmin = 1, 1, float('inf')
factor = 2

while n != 1:
    cur = 0
    flag = False
    while n % factor == 0:
        n = n // factor
        cur += 1
        flag = True
    if flag:
        factors *= factor
        mmin = min(mmin, cur)
    mmax = max(mmax, cur)
    factor += 1
mmin = min(mmin, mmax)
#print(factors, mmax, mmin)
i = 0
while math.pow(2, i) < mmax:
    i += 1

if mmax != math.pow(2, i) or mmin != math.pow(2, i):
    i += 1
print(factors, i)
