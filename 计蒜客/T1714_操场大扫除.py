line = input()
n, m, b, g = [int(item) for item in line.strip().split()]
rows = []
cols = []
for i in range(b):
    line = input()
    x, y = int(line.strip().split()[0]), int(line.strip().split()[1])
    rows.extend(list(range(x, y+1)))
rows = list(set(rows))
for i in range(g):
    line = input()
    x, y = int(line.strip().split()[0]), int(line.strip().split()[1])
    cols.extend(list(range(x, y+1)))
cols = list(set(cols))

res = len(rows) * m + len(cols) * (n - len(rows))
print(res)