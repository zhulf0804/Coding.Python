n = int(input())
a = input()

sums = []
summ = 0
for i in range(n):
    cur = int(a[i])
    summ += cur
    sums.append(summ)

ok = False
if sums[-1] == 0:
    ok = True
for i in range(901):
    if ok:
        break
    first = False
    st = 0
    j = 0
    while j < n:
        summ = sums[j] - sums[st] + int(a[st])
        if summ == i:
            if first and sums[-1] - sums[j] == 0:
                ok = True
                #print(i)
            first = True
            st = j + 1
            j += 1
            while j < n and a[j] == '0':
                j += 1
        elif summ > i:
            break
        else:
            j += 1
if ok:
    print("YES")
else:
    print("NO")