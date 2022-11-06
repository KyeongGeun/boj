class l_list:
    stack = []

    def __init__(self, n, k):
        self.st = ['O'] * n
        self.lst = [node() for _ in range(n)]

        for i in range(n):
            self.lst[i].idx = i

        for i in range(n - 1):
            self.lst[i].right = self.lst[i + 1]
            self.lst[i + 1].left = self.lst[i]

        self.cur = self.lst[k]

    def up(self, n):
        for _ in range(n):
            if not self.cur.left:
                break
            self.cur = self.cur.left

    def down(self, n):
        for _ in range(n):
            if not self.cur.right:
                break
            self.cur = self.cur.right

    def delete(self):
        left = None
        if self.cur.left:
            left = self.cur.left

        right = None
        if self.cur.right:
            right = self.cur.right

        if left and right:
            left.right = right
            right.left = left
        elif left:
            left.right = None
        elif right:
            right.left = None

        self.st[self.cur.idx] = 'X'
        self.stack.append(self.cur)

        if right:
            self.cur = right
        else:
            self.cur = left

    def ctrl_z(self):
        node = self.stack.pop()
        self.st[node.idx] = 'O'
        if node.left:
            node.left.right = node
        if node.right:
            node.right.left = node

    def __str__(self):
        return ''.join(self.st)


class node:
    left = None
    right = None
    idx = None


def solution(n, k, cmd):
    li = l_list(n, k)
    for s in cmd:
        lst = s.split()
        if lst[0] == 'U':
            li.up(int(lst[1]))
        elif lst[0] == 'D':
            li.down(int(lst[1]))
        elif lst[0] == 'C':
            li.delete()
        else:
            li.ctrl_z()

    return str(li)
