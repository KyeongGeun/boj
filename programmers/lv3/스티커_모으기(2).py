def solution(sticker):
    if len(sticker) < 3:
        return max(sticker)

    y, z = sticker[0], max(sticker[1], sticker[0] + sticker[2])
    b, c = sticker[1], max(sticker[1], sticker[2])

    for k in sticker[3:]:
        y, z = z, max(z, y + k)
        b, c = c, max(c, b + k)

    return max(y, c)
