class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s))

        def recur(i=0):
            if i == len(s):
                return 1
            if dp[i] != -1:
                return dp[i]
            if s[i] == '0':
                return 0

            ret = 0
            if i + 1 < len(s) and ((int(s[i]) == 2 and int(s[i + 1]) <= 6) or int(s[i]) == 1):
                ret += recur(i + 2)
            ret += recur(i + 1)

            dp[i] = ret
            return ret

        return recur()
