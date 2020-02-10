n = int(input())
words = input().strip().split()
d = []
for word in words:
    if set(word) not in d:
        d.append(set(word))

print(len(d))