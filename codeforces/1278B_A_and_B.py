t = int(input())
for i in range(t):
    line = input()
    a, b = int(line.strip().split()[0]), int(line.strip().split()[1])
    d = abs(a - b)
    summ = 0
    i = 0
    while summ < d:
        i += 1
        summ += i

    if (summ - d) % 2 == 0:
        print(i)
    else:
        if i % 2 == 0:
            print(i + 1)
        else:
            print(i + 2)