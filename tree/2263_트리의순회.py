import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

in_o = list(map(int, input().split()))
po_o = list(map(int, input().split()))

index = [-1] * (n + 1)
for i in range(n):
    index[in_o[i]] = i

def pre(in_start, in_end, po_start, po_end):

    if po_start >= po_end:
        return

    idx = index[po_o[po_end - 1]]

    print(po_o[po_end - 1], end=' ')

    length = idx - in_start

    pre(in_start, idx, po_start, po_start + length)
    pre(idx + 1, in_end, po_start + length, po_end - 1)

pre(0, n, 0, n)