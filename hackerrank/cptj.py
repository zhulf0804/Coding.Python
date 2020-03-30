n = int(input())
words = input().split()
d = {}
for word in words:
    d[word] = d.get(word, 0) + 1
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

for i in range(20):
    print(d[i][0])