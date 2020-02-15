import sys
input=sys.stdin.readline

n = int(input())

ls = []
for i in range(n):
    l, r = list(map(int, input().strip().split()))
    ls.append([l, r, i])
ls = sorted(ls, key=lambda x: (x[0], -x[1]))
flag = False
mmax = -1
arg_mother = 0
for i in range(n):
    cur_l, cur_r, child = ls[i]
    if cur_r <= mmax:
        print(child + 1, arg_mother + 1)
        flag = True
        break
    else:
        mmax = cur_r
        arg_mother = ls[i][2]

if not flag:
    print(-1, -1)

'''
import sys
input=sys.stdin.readline

n = int(input())

ls = []
for i in range(n):
    l, r = list(map(int, input().strip().split()))
    ls.append([l, r, i])
ls = sorted(ls, key=lambda x: (x[0], -x[1]))
flag = False
for i in range(n-1):
    cur_l, cur_r, mother = ls[i]
    if cur_r >= ls[i+1][1]:
        print(ls[i+1][2] + 1, mother + 1)
        flag = True
        break

if not flag:
    print(-1, -1)
'''