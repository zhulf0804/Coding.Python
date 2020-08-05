n = int(input())
s = input()
n = n // 3

d = {}
for item in s:
    d[item] = d.get(item, 0) + 1

d2 = [0, 0, 0]
res = []
for item in s:
    if d[item] <= n:
        res.append(item)
        continue
    if d[item] > n:
        ok = True
        for i in ['0', '1', '2']:
            if d.get(i, 0) < n:
                if d2[int(item)] >= n or i < item:
                    d[item] -= 1
                    d[i] = d.get(i, 0) + 1
                    res.append(i)
                else:
                    d2[int(item)] += 1
                    res.append(item)
                break

print(''.join(map(str, res)))