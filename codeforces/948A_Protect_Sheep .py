import copy


R, C = list(map(int, input().strip().split()))
#print(R, C)
maps = []
ls, lw = 0, 0
for i in range(R):
    line = input().strip()
    tmp = []
    for item in line:
        if item == 'S':
            ls += 1
        elif item == 'W':
            lw += 1
        tmp.append(item)
    maps.append(tmp)
#print(maps)
results = copy.deepcopy(maps)

danger = False
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'S':
            if j - 1 >= 0:
                if maps[i][j-1] == '.':
                    results[i][j-1] = 'D'
                elif maps[i][j-1] == 'W':
                    danger = True
                    break
            if j + 1 < C:
                if maps[i][j+1] == '.':
                    results[i][j+1] = 'D'
                elif maps[i][j+1] == 'W':
                    danger = True
                    break
            if i - 1 >= 0:
                if maps[i-1][j] == '.':
                    results[i-1][j] = 'D'
                elif maps[i-1][j] == 'W':
                    danger = True
                    break
            if i + 1 < R:
                if maps[i+1][j] == '.':
                    results[i+1][j] = 'D'
                elif maps[i+1][j] == 'W':
                    danger = True
                    break
if danger:
    print("No")
else:
    print("Yes")
    for i in range(R):
        print(''.join(results[i]))