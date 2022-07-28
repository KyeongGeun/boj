import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [-1] * (n + 1)
know = list(map(int, input().split()))
for i in range(1, len(know)):
    parent[know[i]] = 0

party = []
for _ in range(m):
    party.append(list(map(int, input().split())))

party.sort(reverse=True)

ans = len(party)
flag = True
while flag:
    flag = False
    for li in party:
        if li[0] == 0:
            continue
        for i in range(1, len(li)):
            if parent[li[i]] == 0:
                flag = True
                li[0] = 0
                ans -= 1
                for i in range(1, len(li)):
                    parent[li[i]] = 0
                break

print(ans)
