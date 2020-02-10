nums = list(map(int, input().strip().split()))
mmax = 0
for i in range(14):
    score = 0
    cur = nums[i]
    if cur == 0:
        continue
    for j in range(14):
        dist = j - i
        if j <= i:
            dist = 14 - i + j
        if cur % 14 < dist:
            add = cur // 14
        else:
            add = cur // 14 + 1
        if j == i:
            tmp = add
        else:
            tmp = nums[j] + add
        if tmp % 2 == 0:
            score += tmp
        print(add)
    #print(score)
    mmax = max(mmax, score)

print(mmax)