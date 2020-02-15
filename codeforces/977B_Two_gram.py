n = int(input())
S = input().strip()
d = {}
for i in range(n-1):
    cur = S[i:i+2]
    d[cur] = d.get(cur, 0) + 1

ans = S[:2]
mmax = 1
for key, val in d.items():
    if val > mmax:
        mmax = val
        ans = key
print(ans)