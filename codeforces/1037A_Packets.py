import math


n = int(input())
cur = 0
summ = 0
while summ < n:
    summ += math.pow(2, cur)
    cur += 1
print(cur)



'''
def helper(n):
    # k * (k + 1) = 2 * n > k * k
    # k < sqrt(2 * n)
    # k <= floor(sqrt(2 * n))
    cur = math.floor(math.sqrt(2 * n))
    while cur * (cur + 1) > 2 * n:
        cur -= 1
    left = n - cur * (cur + 1) // 2
    return cur, left

n = int(input())
res = 0
while n != 0:
    cur, n = helper(n)
    res += cur

print(res)
'''