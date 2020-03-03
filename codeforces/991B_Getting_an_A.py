n = int(input())
scores = list(map(int, input().strip().split()))

scores = sorted(scores)

goal = n * 4.5
summ = 0
for i in range(n):
    summ += scores[i]

res = -1
for i in range(n):
    if summ >= goal:
        res = i
        break
    else:
        summ = summ - scores[i] + 5

if res == -1:
    print(n)
else:
    print(res)