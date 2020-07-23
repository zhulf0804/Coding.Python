t = int(input())
for _ in range(t):
    n = int(input())
    a, b = list(map(int, input())), list(map(int, input()))
    ans, res = 0, []
    for j in range(n-1, -1, -1):
        if a[j] == b[j]:
            continue
        if a[0] == b[j]:
            res.append(1)
            ans += 1
            a[0] = 1 - a[0]
        ans += 1
        res.append(j + 1)
        for k in range(j+1):
            a[k] = 1 - a[k]
        a[:j + 1] = reversed(a[:j + 1])
    print(ans, ' '.join(map(str, res)))



# (k1^2 + k2^2 + ... + kt^2)* (1 + 1 + ... ) >= n^2
# n^2 >= k1^2 + k2^2 + ... + kt^2 >= n