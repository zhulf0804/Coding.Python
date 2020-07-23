t = int(input())
for _ in range(t):
    n = int(input())
    a, b = list(map(int, input())), list(map(int, input()))
    ans, res = 0, []
    l, r, num = 0, n - 1, 0
    for j in range(n-1, -1, -1):
        a0, ai = a[l] ^ (num % 2), a[r] ^ (num % 2)
        if num % 2 != 0:
            a0, ai = ai, a0
        if ai == b[j]:
            if num % 2 == 0:
                r -= 1
            else:
                l += 1
            continue
        if a0 == b[j]:
            ans += 1
            res.append(1)
        res.append(j+1)
        ans += 1
        num += 1
        if num % 2 == 0:
            r -= 1
        else:
            l += 1

    print(ans, ' '.join(map(str, res)))

'''
1 * 0 = 1
0 * 0 = 0
1 * 1 = 0
0 * 1 = 1 
'''