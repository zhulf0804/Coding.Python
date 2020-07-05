n = int(input())
s = input()

res = []
i, step = 0, 1
while i < n:
    res.append(s[i])
    i += step
    step += 1
print(''.join(res))