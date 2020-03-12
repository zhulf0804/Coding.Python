n = int(input())
cur = 0
res = 0
for i in range(n):
    a, b, c, d = list(map(int, input().strip().split()))
    score = a + b + c + d
    if i == 0:
       cur = score
    else:
       if score > cur:
           res += 1
print(res + 1)