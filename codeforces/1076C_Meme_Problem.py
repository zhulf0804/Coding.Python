import math

t = int(input())

def helper(x):
    return x * x - 4 * x


for _ in range(t):
    d = int(input())
    delta = helper(d)
    if delta < 0:
        print('N')
    else:
        line = ['Y']
        a = (d - math.sqrt(delta)) / 2
        b = d - a
        line.append(str(a))
        line.append(str(b))
        print(' '.join(line))