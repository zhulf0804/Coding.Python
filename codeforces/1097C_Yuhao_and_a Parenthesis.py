import sys
input = sys.stdin.readline

n = int(input())
v = []
for _ in range(n):
    bkt = input()
    l, r, mmin = 0, 0, float('inf')
    for item in bkt:
        if item == '(':
            l += 1
        elif item == ')':
            r += 1
        mmin = min(mmin, l - r)
    v.append([l-r, mmin])

v = sorted(v, key=lambda x:(x[0], x[1]))
ans = 0
l, r = 0, n-1
while l < r:
    ll, llm = v[l]
    rr, rrm = v[r]
    if rr < 0 or ll > 0:
        break
    if ll + rr > 0:
        r -= 1
    elif ll + rr < 0:
        l += 1
    else:
        if rrm < 0:
            r -= 1
        else:
            if rr + llm >= 0:
                ans += 1
                l += 1
                r -= 1
            else:
                l += 1
print(ans)