import sys
input = sys.stdin.readline

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    ws = list(map(int, input().split()))
    degs = [0] * n
    for i in range(n - 1):
        a, b = list(map(int, input().split()))
        degs[a-1] += 1
        degs[b-1] += 1

    vals = [[ws[i], degs[i]-1] for i in range(n)]
    vals = sorted(vals)
    res, summ, cur, x = [], sum(ws), 0, -1
    for i in range(n-1):
        ans = summ + cur
        res.append(ans)
        if i < n - 2:
            while vals[x][1] <= 0:
                x -= 1
            vals[x][1] -= 1
            cur += vals[x][0]
    print(' '.join(map(str, res)))