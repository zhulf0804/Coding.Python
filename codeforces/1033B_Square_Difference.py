import math


T = int(input())


def is_prime(n):
    if n == 2 or n == 3:
        return True
    upper = int(math.sqrt(n)) + 1
    for i in range(2, upper + 1):
        if n % i == 0:
            return False
    return True


for i in range(T):
    x, y = list(map(int, input().split()))
    if x - y > 1:
        print("NO")
        continue
    z = x + y
    if is_prime(z):
        print("YES")
    else:
        print("NO")