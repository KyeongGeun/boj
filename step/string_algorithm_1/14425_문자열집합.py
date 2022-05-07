import sys
input = sys.stdin.readline


class trie:
    head = [False] * 27

    def add(self, s):
        cur = self.head
        for v in s:
            n = ord(v) - 97
            if not cur[n]:
                cur[n] = [False] * 27
            cur = cur[n]

        cur[26] = True

    def search(self, s):
        cur = self.head
        for v in s:
            n = ord(v) - 97
            if not cur[n]:
                return False
            cur = cur[n]

        return cur[26]


n, m = map(int, input().split())
tr = trie()

for _ in range(n):
    tr.add(input().rstrip())

cnt = 0
for _ in range(m):
    if tr.search(input().strip()):
        cnt += 1

print(cnt)
