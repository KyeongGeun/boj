class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        li = []

        def recur(idx=0):
            if idx == len(s):
                if len(li) == 4:
                    ans.append('.'.join(li))
                return

            sset = set()
            sset.add((s[idx], idx + 1))
            if s[idx] != '0':
                if int(s[idx:idx + 2]) < 256:
                    sset.add((s[idx:idx + 2], min(len(s), idx + 2)))
                if int(s[idx:idx + 3]) < 256:
                    sset.add((s[idx:idx + 3], min(len(s), idx + 3)))

            for st, i in sset:
                li.append(st)
                recur(i)
                li.pop()

        recur()
        return ans
