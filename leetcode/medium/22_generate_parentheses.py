class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def recur(l, r, cur):
            if l == r == 0:
                ans.append(''.join(cur))
                return ans

            if l > 0:
                cur.append('(')
                recur(l - 1, r + 1, cur)
                cur.pop()
            if r > 0:
                cur.append(')')
                recur(l, r - 1, cur)
                cur.pop()

        recur(n, 0, [])
        return ans
