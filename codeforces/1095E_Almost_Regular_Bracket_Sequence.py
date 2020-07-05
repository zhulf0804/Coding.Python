n, s = int(input()), input()

diff, cura, curb = [], 0, 0
for item in s:
    if item == '(':
        cura += 1
    else:
        curb += 1
    diff.append(cura - curb)
ans = 0
if diff[-1] == 2:
    if min(diff) >= 0:
        ans, i = 0, n - 1
        while i >= 0 and diff[i] >= 2:
            if s[i] == '(':
                ans += 1
            i -= 1
elif diff[-1] == -2:
    if min(diff) >= -2:
        ans, i = 0, 0
        while i < n and diff[i] >= 0:
            if s[i] == ')':
                ans += 1
            i += 1
        if i < n and s[i] == ')' and diff[i] < 0:
            ans += 1
print(ans)