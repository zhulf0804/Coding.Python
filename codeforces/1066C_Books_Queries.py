q = int(input())
L, R, nums = [], [], []
for _ in range(q):
    line = input()
    v, a = line.split()[0], int(line.split()[1])
    #print(v, a)
    if v == 'L':
        L.append(a)
    elif v == 'R':
        R.append(a)
    else:
        nums.append([len(L), len(R), a])

all_nl, all_nr = len(L), len(R)
L.reverse()
A = L + R
#print(A)
maps = {a: i for i, a in enumerate(A)}
for num in nums:
    l, r, a = num[0], num[1], num[2]
    nl, nr = maps[a], len(A) - maps[a] - 1
    zl, zr = all_nl - l, all_nr - r
    print(min(nl - zl, nr - zr))