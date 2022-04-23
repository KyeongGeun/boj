import sys
input = sys.stdin.readline


def iscross(l1, l2):

    def in_range(x, y):
        if l1[0] <= x <= l1[2] or l1[2] <= x <= l1[0]:
            if l2[0] <= x <= l2[2] or l2[2] <= x <= l2[0]:
                if l1[1] <= y <= l1[3] or l1[3] <= y <= l1[1]:
                    if l2[1] <= y <= l2[3] or l2[3] <= y <= l2[1]:
                        return True

    v1 = (l1[2] - l1[0], l1[3] - l1[1])
    v2 = (l2[2] - l2[0], l2[3] - l2[1])

    v3 = v1[0] * v2[1] - v1[1] * v2[0]

    if v3 == 0:
        return False

    # y = mx + c
    m1 = v1[1] / v1[0] if v1[0] != 0 else float('inf')
    m2 = v2[1] / v2[0] if v2[0] != 0 else float('inf')

    c1 = l1[1] - m1 * l1[0]
    c2 = l2[1] - m2 * l2[0]

    # m1x + c1 = m2x + c2
    # (m1 - m2)x = c2 - c1
    # x = (c2 - c1) / (m1 - m2)
    px = (c2 - c1) / (m1 - m2) if m1 - m2 != 0 else 0
    py = px * m1 + c1

    if m1 == float('inf'):
        px = l1[0]
        py = px * m2 + c2

    if m2 == float('inf'):
        px = l2[0]
        py = px * m1 + c1

    if not in_range(px, py):
        return False

    return True


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

if iscross(l1, l2):
    print(1)
else:
    print(0)
