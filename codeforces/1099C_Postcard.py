s, k = input(), int(input())

a, b, c = 0, 0, 0
for item in s:
    if item == '?':
        a += 1
    elif item == '*':
        b += 1
    else:
        c += 1

if c - a - b > k or (b == 0 and c < k):
    print('Impossible')
else:
    res, n = [], len(s)
    if c > k:
        diff = c - k
        for i in range(n):
            if s[i] == '?' or s[i] == '*':
                continue
            if i == n - 1:
                res.append(s[i])
                continue
            if s[i + 1] == '?' or s[i + 1] == '*':
                if diff > 0:
                    diff -= 1
                else:
                    res.append(s[i])
            else:
                res.append(s[i])
    else:
        diff = k - c
        for i in range(n):
            if s[i] == '?' or s[i] == '*':
                continue
            if i == n - 1:
                res.append(s[i])
                continue
            if s[i + 1] == '*':
                if diff > 0:
                    res.append(s[i] * (diff + 1))
                    diff = 0
                else:
                    res.append(s[i])
            else:
                res.append(s[i])
    print(''.join(res))