# https://www.hackerrank.com/contests/2020-deepglint/challenges/challenge-2397/problem

n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i] % n

wa = zip(w, a)
wa = sorted(wa, key=lambda x: x[0])
#print(wa)
b = [item[1] for item in wa]

ok = False
d = {}
cur = b[0]
while cur not in d:
    d[cur] = 1
    cur = b[cur]

res = []
d = {}
while cur not in d:
    d[cur] = 1
    res.append(w.index(cur))
    cur = b[cur]
res = sorted(res)
res = [str(item + 1) for item in res]
print(len(res))
print(' '.join(res))