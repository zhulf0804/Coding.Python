n = int(input())
pairs = []
for _ in range(n):
    pairs.append(list(map(int, input().split())))

res = [1]
while len(res) < n:
    ind = res[-1]
    first, second = pairs[ind - 1]
    #print(first, second)
    if first in pairs[second - 1]:
        res.append(second)
        res.append(first)
    else:
        res.append(first)
        res.append(second)
print(' '.join(map(str, res[:n])))