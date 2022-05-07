import sys
input = sys.stdin.readline


class trie:
    head = {}

    def add(self, li):
        cur = self.head
        for v in li:
            if not v in cur:
                cur[v] = {}
            cur = cur[v]

    def tostring(self, k=head, n=0):
        s = '--' * n
        for v in sorted(k.keys()):
            print(s + v)
            self.tostring(k[v], n + 1)


n = int(input())
tr = trie()

for _ in range(n):
    li = input().split()
    tr.add(li[1:])

tr.tostring()
