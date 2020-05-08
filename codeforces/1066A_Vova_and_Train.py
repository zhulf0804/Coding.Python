T = int(input())
for _ in range(T):
    N, V, L, R = list(map(int, input().split()))
    n = N // V
    m1 = (L - 1) // V
    m2 = R // V
    print(n - (m2 - m1))