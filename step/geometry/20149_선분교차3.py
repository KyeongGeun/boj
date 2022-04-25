import sys
input = sys.stdin.readline
err = 0.00000001


def iscross(l1, l2):
    def in_range(x, y):
        if min(l1[0], l1[2]) - err <= x <= max(l1[0], l1[2]) + err:
            if min(l2[0], l2[2]) - err <= x <= max(l2[0], l2[2]) + err:
                if min(l1[1], l1[3]) - err <= y <= max(l1[1], l1[3]) + err:
                    if min(l2[1], l2[3]) - err <= y <= max(l2[1], l2[3]) + err:
                        return True
        return False

    v1 = (l1[2] - l1[0], l1[3] - l1[1])
    v2 = (l2[2] - l2[0], l2[3] - l2[1])

    v3 = v1[0] * v2[1] - v1[1] * v2[0]

    if -err <= v3 <= err:
        if in_range(l1[0], l1[1]) or in_range(l1[2], l1[3]) or in_range(l2[0], l2[1]) or in_range(l2[2], l2[3]):
            if l2[2] - err <= l1[0] <= l2[2] + err and l2[3] - err <= l1[1] <= l2[3] + err:
                answer.extend([l1[0], l1[1]])
            elif l2[0] - err <= l1[2] <= l2[0] + err and l2[1] - err <= l1[3] <= l2[1] + err:
                answer.extend([l1[2], l1[3]])
            return True
        else:
            return False

    # y = mx + c
    m1 = v1[1] / v1[0] if v1[0] != 0 else float('inf')
    m2 = v2[1] / v2[0] if v2[0] != 0 else float('inf')

    c1 = l1[1] - m1 * l1[0]
    c2 = l2[1] - m2 * l2[0]

    # m1x + c1 = m2x + c2
    # (m1 - m2)x = c2 - c1
    # x = (c2 - c1) / (m1 - m2)
    px = (c2 - c1) / (m1 - m2)
    py = px * m1 + c1

    if m1 == float('inf'):
        px = l1[0]
        py = px * m2 + c2

    elif m2 == float('inf'):
        px = l2[0]
        py = px * m1 + c1

    if not in_range(px, py):
        return False

    answer.extend([px, py])
    return True


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

if l1[0] > l1[2] or (l1[0] == l1[2] and l1[1] > l1[3]):
    l1[0], l1[1], l1[2], l1[3] = l1[2], l1[3], l1[0], l1[1]
if l2[0] > l2[2] or (l2[0] == l2[2] and l2[1] > l2[3]):
    l2[0], l2[1], l2[2], l2[3] = l2[2], l2[3], l2[0], l2[1]

answer = []
if iscross(l1, l2):
    print(1)
    if answer:
        print(*answer)
else:
    print(0)
