line = input()
high, up, down = [int(item) for item in line.strip().split()]
#print(high, up, down)
summ = up
d = 1
while summ < high:
    summ -= down
    summ += up
    d += 1
print(d)