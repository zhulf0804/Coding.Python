n, s = int(input()), input()
if n <= 1:
    print("NO")
else:
    d = {}
    loc = -1
    d[s[0]] = 1
    for i in range(1, n):
        if s[i] not in d:
            loc = i - 1
            break
    if loc == -1:
        print('NO')
    else:
        print("YES")
        print(s[loc: loc+2])