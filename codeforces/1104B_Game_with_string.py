s = input()
n = len(s)
stack, top = [s[0]] * n, 0
num = 0
for i in range(1, n):
    if top >= 0 and s[i] == stack[top]:
        num += 1
        top -= 1
        continue
    top += 1
    stack[top] = s[i]

if num % 2 == 0:
    print("No")
else:
    print("Yes")