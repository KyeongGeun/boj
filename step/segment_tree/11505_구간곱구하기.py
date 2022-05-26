import sys
input = sys.stdin.readline
MOD = 1000000007

def make(x, i, j):
    if i == j:
        seg[x] = li[i]
        return seg[x]
    
    mid = (i + j) // 2
    seg[x] = make(x * 2 + 1, i, mid) * make(x * 2 + 2, mid + 1, j)
    seg[x] %= MOD
    return seg[x]


def update(x, i, j, idx, c):
    if i > idx or j < idx:
        return

    if i == j:
        seg[x] = c
        return
    
    mid = (i + j) // 2
    update(x * 2 + 1, i, mid, idx, c)
    update(x * 2 + 2, mid + 1, j, idx, c)

    seg[x] = seg[x * 2 + 1] * seg[x * 2 + 2] % MOD


def ssum(x, i, j, b, c):
    if b > j or c < i:
        return 1
    elif b <= i and j <= c:
        return seg[x] % MOD
    
    mid = (i + j) // 2
    ret = ssum(x * 2 + 1, i, mid, b, c) * ssum(x * 2 + 2, mid + 1, j, b, c)
    return ret % MOD

n, m, k = map(int, input().split())

li = [int(input()) for _ in range(n)]
seg = [1] * (n * 4)

make(0, 0, n - 1)

ans = []
for _ in range(m + k):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        update(0, 0, n - 1, b, c)
        li[b] = c
    elif a == 2:
        c -= 1
        ans.append(ssum(0, 0, n - 1, b, c))

print(*ans, sep='\n')
