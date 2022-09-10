import sys
input = sys.stdin.readline

ans = []
for case in range(1, int(input()) + 1):
    n = int(input())

    li = [list(map(int, input().split())) for _ in range(n)]
    li.sort(key=sum)

    bitSet = 1
    for p, s in li:
        if s == 0:
            continue

        bitSet |= (bitSet & ((1 << p + 1) - 1)) << s

    ans.append(f'Case #{case}: {bitSet.bit_length() - 1}')

print('\n'.join(ans))
