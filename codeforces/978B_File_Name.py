n = int(input())
s = input()
st = 0
res = 0
for i in range(n):
    if s[i] == 'x' and (i == 0 or s[i - 1] != 'x'):
        st = i
    if s[i] == 'x' and (i == n - 1 or s[i+1] != 'x'):
        cur_len = i - st + 1
        #print(st, i)
        if cur_len >= 3:
            res += cur_len - 2

print(res)
