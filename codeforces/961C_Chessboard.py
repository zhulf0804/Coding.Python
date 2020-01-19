n = int(input())

pieces = []
recolors = []
for i in range(4):
    piece = []
    for j in range(n):
        line = input().strip()
        piece.append(line)
    if i != 3:
        input()
    pieces.append(piece)
    cur1 = 0
    for x in range(n):
        for y in range(n):
            cur1 += (x + y + int(piece[x][y])) % 2
    cur2 = 0
    for x in range(n):
        for y in range(n):
            cur2 += (x + y + 1 + int(piece[x][y])) % 2
    recolors.append([cur1, cur2])

#print(recolors)

mmin = (2 * n) * (2 * n)
enums = [[[0, 1], [2, 3]],
         [[0, 2], [1, 3]],
         [[0, 3], [1, 2]],
         [[1, 2], [0, 3]],
         [[1, 3], [0, 2]],
         [[2, 3], [0, 1]]]
for i in range(len(enums)):
    a, b = enums[i]
    #print(a, b, recolors)
    summ = recolors[a[0]][0] + recolors[a[1]][0] + recolors[b[0]][1] + recolors[b[1]][1]
    mmin = min((mmin, summ))
print(mmin)