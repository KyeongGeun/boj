class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = {}
        for c in secret:
            dic.setdefault(c, 0)
            dic[c] += 1

        a = 0
        for s, g in zip(secret, guess):
            if s == g:
                a += 1

                dic[g] -= 1
                if dic[g] == 0:
                    del dic[g]

        b = 0
        for s, g in zip(secret, guess):
            if g not in dic or s == g:
                continue

            b += 1

            dic[g] -= 1
            if dic[g] == 0:
                del dic[g]

        return f'{a}A{b}B'
