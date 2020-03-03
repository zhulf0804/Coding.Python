n = int(input())
res = 0
i = 0
coins = [100, 20, 10, 5, 1]
while n > 0:
    cur = n // coins[i]
    res += cur
    n -= cur * coins[i]
    i += 1
print(res)