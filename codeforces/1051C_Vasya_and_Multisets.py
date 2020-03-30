from collections import Counter


n = int(input())
s = list(map(int, input().split()))

count = Counter(s)
count_1 = 0
count_2 = 0
for i in range(n):
    if count[s[i]] == 1:
        count_1 += 1
    if count[s[i]] == 2:
        count_2 += 1

if count_1 % 2 == 1 and count_1 + count_2 == n:
    print("NO")
else:
    print("YES")
    res = []
    cls = ['A', 'B']
    cur = 0
    if count_1 % 2 == 0:
        for i in range(n):
            if count[s[i]] == 1:
                res.append(cls[cur % 2])
                cur += 1
            else:
                res.append('B')
    else:
        need = True
        for i in range(n):
            if count[s[i]] == 1:
                res.append(cls[cur % 2])
                cur += 1
            elif need and count[s[i]] > 2:
                res.append('B')
                need = False
            else:
                res.append('A')
    print(''.join(res))