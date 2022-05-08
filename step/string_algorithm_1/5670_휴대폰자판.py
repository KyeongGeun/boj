import sys
input = sys.stdin.readline


class trie:
    head = {}
    cnt = 0

    def cclear(self):
        self.head.clear()
        self.cnt = 0

    def add(self, s):
        cur = self.head
        for v in s:
            if not v in cur:
                cur[v] = {}
            cur = cur[v]

        cur['*'] = True

    def cal(self, d=head):
        for v in d.keys():
            if v == '*':
                self.cnt += 1
                continue
            self.cal2(d[v], 1)

    def cal2(self, d, n):
        while len(d) == 1 and not '*' in d:
            d = d[list(d.keys())[0]]

        for v in d.keys():
            if v == '*':
                self.cnt += n
                continue
            self.cal2(d[v], n + 1)


tr = trie()
while True:
    try:
        n = int(input())
    except:
        break

    tr.cclear()
    for _ in range(n):
        tr.add(input().rstrip())
    tr.cal()

    print(f'{tr.cnt / n:.2f}')
