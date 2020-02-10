n = int(input())
s = input()
c0 = 0
for i in s:
    if i == '0':
        c0 += 1
c1 = n - c0
if c0 == 0:
    print('1')
elif c1 == 0:
    print(s)
else:
    print('1' + '0'*c0)