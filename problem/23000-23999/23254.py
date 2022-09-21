import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n *= 24

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dic = dict()
for i in range(m):
    c, d = (100 - a[i]) // b[i], (100 - a[i]) % b[i]
    dic.setdefault(b[i], 0)
    dic.setdefault(d, 0)
    dic[b[i]] += c
    dic[d] += 1

li = list(dic.items())
li.sort(key=lambda x: -x[0])

ans = sum(a)
cnt = 0

for a, b in li:
    if cnt + b < n:
        ans += a * b
        cnt += b
    else:
        ans += a * (n - cnt)
        break


print(ans)
