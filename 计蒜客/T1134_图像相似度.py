line = input()
m, n = int(line.strip().split()[0]), int(line.strip().split()[1])
im1 = [[] for i in range(m)]
#im2 = list(im1)
im2 = [[] for i in range(m)]

for i in range(m):
    line = input()
    im1[i].extend(line.strip().split())
for i in range(m):
    line = input()
    im2[i].extend(line.strip().split())

count = 0
for i in range(m):
    for j in range(n):
        if im1[i][j] == im2[i][j]:
            count += 1
res = count / (m * n) * 100
print("%.2f"%res)