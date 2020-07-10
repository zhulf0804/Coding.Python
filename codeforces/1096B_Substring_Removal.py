n, s = int(input()), input()

l = 0
while l < n:
    if s[l] != s[0]:
        break
    l += 1

r = 0
while n - 1 - r >= 0:
    if s[n - 1 - r] != s[-1]:
        break
    r += 1

ans = l + r + 1
if s[0] == s[-1]:
    ans = ((l + 1) * (r + 1)) % 998244353
print(ans)