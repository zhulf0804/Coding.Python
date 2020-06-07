# https://codeforces.com/problemset/problem/1081/D

import sys
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))
x = list(map(int, input().split()))

uf = [-1 for _ in range(n+1)]

def find(p, uf):
    if uf[p] < 0:
        return p
    uf[p] = find(uf[p], uf)
    return uf[p]

def union(p, q, uf, specials):
    proot = find(p, uf)
    qroot = find(q, uf)
    if proot == qroot:
        return
    elif uf[proot] > uf[qroot]:
        uf[qroot] += uf[proot]
        uf[proot] = qroot
        specials[qroot] = specials[qroot] or specials[proot]
    else:
        uf[proot] += uf[qroot]
        uf[qroot] = proot
        specials[proot] = specials[qroot] or specials[proot]

edges = []
for _ in range(m):
    u, v, w = list(map(int, input().split()))
    edges.append((w, u, v))
edges = sorted(edges, key=lambda item: item[0])
specials = [0] * (n + 1)
for item in x:
    specials[item] = 1

ans = -1
for w, u, v in edges:
    ufather, vfather = find(u, uf), find(v, uf)
    if ufather != vfather:
        if specials[ufather] == 1 and specials[vfather] == 1:
            ans = max(ans, w)
        union(u, v, uf, specials)

res = [ans] * k
print(' '.join(map(str, res)))