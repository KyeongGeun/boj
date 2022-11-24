class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)

        ret = ''
        cur = s[0]
        cnt = 0
        for v in s:
            if v == cur:
                cnt += 1
            else:
                ret += str(cnt) + str(cur)
                cur = v
                cnt = 1

        if cnt > 0:
            ret += str(cnt) + str(cur)

        return ret
