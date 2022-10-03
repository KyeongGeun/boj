bits = set()


def dfs(i, s, trie, idx):
    if i == len(s):
        if '.' in trie:
            trie['.'].append(idx)
        return

    if s[i] == '*':
        for k in trie:
            if k == '.':
                continue
            dfs(i + 1, s, trie[k], idx)
    elif s[i] in trie:
        dfs(i + 1, s, trie[s[i]], idx)


def recur(i, li, visited, bit):
    if i == len(li):
        if False not in visited:
            bits.add(bit)
        return

    for v in li[i]:
        if visited[v]:
            continue

        temp = (1 << i)

        visited[v] = True
        bit |= temp

        recur(i + 1, li, visited, bit)

        visited[v] = False
        bit ^= temp

    recur(i + 1, li, visited, bit)


def solution(user_id, banned_id):
    trie = dict()

    li = []

    for s in user_id:
        temp = trie
        for c in s:
            temp.setdefault(c, dict())
            temp = temp[c]
        temp['.'] = []
        li.append(temp['.'])

    for idx, s in enumerate(banned_id):
        dfs(0, s, trie, idx)

    visited = [False] * len(banned_id)
    recur(0, li, visited, 0)

    return len(bits)
