t = int(input())
for i in range(t):
    n = int(input())
    line = input()
    nums = [int(item) for item in line.strip().split()]
    a, b = 0, 0
    dpa,  dpb = [0] * (2 * n), [0] * (2 * n)
    for j in range(2 * n):
        if nums[j] == 1:
            a += 1
        elif nums[j] == 2:
            b += 1
        dpa[j] = a
        dpb[j] = b
    if a == b:
        print(0)
        continue
    d = a - b
    dict = {}
    for j in range(n, 2*n):
        cura = dpa[j] - dpa[n]
        curb = dpb[j] - dpb[n]
        if nums[n] == 1:
            cura += 1
        else:
            curb += 1
        diff = cura - curb
        if diff not in dict:
            dict[diff] = j - n + 1

    mmin = float('inf')
    for x in range(n-1, -1, -1):
        cura = dpa[n-1] - dpa[x]
        curb = dpb[n-1] - dpb[x]
        if nums[x] == 1:
            cura += 1
        else:
            curb += 1
        diff = cura - curb
        if diff == d:
            mmin = min(mmin, n - x)
            break
        if d - diff in dict:
            mmin = min(mmin, dict[d-diff] + n - x)
    if d in dict:
        mmin = min(mmin, dict[d])
    print(mmin)