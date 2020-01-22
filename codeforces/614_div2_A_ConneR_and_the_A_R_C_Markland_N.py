t = int(input())
for i in range(t):
    n, s, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    d = {}
    for item in a:
        d[item] =  1
    i = 0
    while i < 1001:
        if s - i >= 1 and s-i not in d:
            print(i)
            break
        elif s + i <=n and s+i not in d:
            print(i)
            break
        i += 1