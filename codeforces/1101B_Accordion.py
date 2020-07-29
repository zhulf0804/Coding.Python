s = input()
n = len(s)

l = 0
while l < n:
    if s[l] == '[':
        break
    l += 1

l2 = l + 1
while l2 < n:
    if s[l2] == ':':
        break
    l2 += 1

r = n - 1
while r > 0:
    if s[r] == ']':
        break
    r -= 1

r2 = r - 1
while r2 > 0:
    if s[r2] == ':':
        break
    r2 -= 1

if l2 >= r2:
    print(-1)
else:
    ans = 4
    for i in range(l2+1, r2):
        if s[i] == '|':
            ans += 1
    print(ans)