n = int(input())
a = list(map(int, input().split()))

# t - 1 <= ai <= t + 1
t, ans, p = 1, 1, float('inf')
while t <= 100:
    summ = 0
    for item in a:
        cur = 0
        if item > t + 1:
            cur = item - (t + 1)
        elif item < t - 1:
            cur = (t - 1) - item
        summ += cur
    if summ < p:
        p = summ
        ans = t
    t += 1

print(ans, p)