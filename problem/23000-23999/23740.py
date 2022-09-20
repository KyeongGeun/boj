import sys
input = sys.stdin.readline

n = int(input())

li = [tuple(map(int, input().split())) for _ in range(n)]

li.sort()

s, e, c = li[0]

ans = []
for s1, e1, c1 in li:
    if e < s1:
        ans.append(f'{s} {e} {c}')
        s, e, c = s1, e1, c1
    else:
        e = max(e, e1)
        c = min(c, c1)

ans.append(f'{s} {e} {c}')

print(len(ans))
print('\n'.join(ans))
