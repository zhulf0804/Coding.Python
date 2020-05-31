t = int(input())


def get_white(xx1, yy1, xx2, yy2):
    h, w = yy2 - yy1 + 1, xx2 - xx1 + 1
    num = (h * w) // 2
    if (xx1 + yy1) % 2 == 0 and (h * w) % 2 == 1:
        num += 1
    return num


for _ in range(t):
    n, m = list(map(int, input().split()))
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, x4, y4 = list(map(int, input().split()))
    white = get_white(1, 1, m, n)
    white1 = get_white(x1, y1, x2, y2)
    white2 = get_white(x3, y3, x4, y4)
    xx1, yy1 = max(x1, x3), max(y1, y3)
    xx2, yy2 = min(x2, x4), min(y2, y4)
    final_white = white + ((y2 - y1 + 1)*(x2 - x1 + 1) - white1)
    tmp = final_white
    if xx1 <= xx2 and yy1 <= yy2:
        z = (xx2 - xx1 + 1) * (yy2 - yy1 + 1)
        white3 = get_white(xx1, yy1, xx2, yy2)
        final_white = final_white - z - (white2 - white3)
    else:
        final_white = final_white - white2
    #print(white, white1, tmp, final_white)
    print(final_white, n * m - final_white)