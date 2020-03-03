d = {}

n = int(input())
summs = []
ok = False

for i in range(n):
    cur_summs = []
    l = int(input())
    nums = list(map(int, input().strip().split()))
    if ok:
        break
    cur = 0
    for j in range(l):
        cur += nums[j]
    summ = cur
    tmp_d = {}

    for j in range(l):
        cur = summ - nums[j]
        cur_summs.append(cur)
        tmp_d[cur] = j + 1
        # print(cur, tmp_d)

    cur_summs = list(set(cur_summs))
    for cur_summ in cur_summs:
        if cur_summ in d:
            ok = True
            print("YES")
            print(d[cur_summ][0], d[cur_summ][1])
            print(i + 1, tmp_d[cur_summ])
            break
        else:
            d[cur_summ] = [i + 1, tmp_d[cur_summ]]
        # d[cur_summ].append([i + 1, tmp_d[cur_summ]])

if not ok:
    print("NO")