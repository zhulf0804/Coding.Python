import math


def helper(x, m, n):
    f = a * x + b
    g = 1 / m * math.exp(x / n)
    return f / g


a, b, c, d = list(map(int, input().split()))

x1 = (d - b / a)
x2 = (c - b / a)
if c == d:
    if x1 <= 0:
        print(0)
    else:
        print(x1)
else:
    critical_v = c * d / (d - c) * math.log(d / c)

    res = critical_v

    #if helper(x1, c, d) > helper(x2, d, c), helper(critical_v, c, d)
    if critical_v - x1 <= 0  and critical_v - x2 <= 0:
        if helper(x1, c, d) > helper(x2, d, c):
            res = x2
        else:
            res = x1
    elif critical_v - x1 >= 0  and critical_v - x2 >= 0:
        if x1 <= 0 and x2 <= 0:
            res = 0
        elif x1 >= 0 and x2 >= 0:
            if helper(x1, c, d) > helper(x2, d, c):
                res = x2
            else:
                res = x1
        elif x1 >= 0 and x2 <= 0:
            if helper(x1, c, d) > helper(0, d, c):
                res = 0
            else:
                res = x1
        elif x1 <= 0 and x2 >= 0:
            if helper(0, c, d) > helper(x2, d, c):
                res = x2
            else:
                res = 0

    print(res)