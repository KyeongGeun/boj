maxv = 0


def recur(k, dungeons, bit, cnt):
    global maxv
    maxv = max(maxv, cnt)

    for i in range(len(dungeons)):
        if bit & (1 << i):
            continue
        if k < dungeons[i][0] or k < dungeons[i][1]:
            continue

        recur(k - dungeons[i][1], dungeons, bit | (1 << i), cnt + 1)


def solution(k, dungeons):
    recur(k, dungeons, 0, 0)
    return maxv
