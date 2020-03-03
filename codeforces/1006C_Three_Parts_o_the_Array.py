n = int(input())
nums = list(map(int, input().strip().split()))

l, r = -1, n
summa, summb = 0, 0
res = 0
while l < r:
    #print(l, summa, r, summb)
    if summa < summb:
       l += 1
       summa += nums[l]
    elif summa > summb:
        r -= 1
        summb += nums[r]
    else:
        l += 1
        r -= 1
        res = summa
        summa += nums[l]
        summb += nums[r]

print(res)