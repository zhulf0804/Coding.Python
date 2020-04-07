n = int(input())
s = input()
n8 = 0
for i in range(n):
    if s[i] == '8':
        n8 += 1

ans = 0
for i in range(n8, 0, -1):
    if (n - i) // 10 >= i:
        ans = i
        break
print(ans)