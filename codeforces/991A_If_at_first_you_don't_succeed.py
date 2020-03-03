A, B, C, N = list(map(int, input().strip().split()))

if C > A or C > B or A >= N or B >= N:
    print(-1)
else:
    passed = A + B - C
    if passed >= N:
        print(-1)
    else:
        print(N - passed)