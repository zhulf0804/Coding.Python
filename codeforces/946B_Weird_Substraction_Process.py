line = input()
a, b = list(map(int, line.strip().split()))

def helper(a, b):
    if a == 0 or b == 0:
        print(a, b)
    else:
        if a >= 2*b:
            times = a // (2*b)
            a -= (times * 2*b)
            helper(a, b)
        elif b >= 2 * a:
            times = b // (2*a)
            b -= (times * 2 * a)
            helper(a, b)
        else:
            print(a, b)

helper(a, b)