class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        li = [[] for _ in range(numRows)]

        for i in range(len(s)):
            j = i % (numRows * 2 - 2)

            if j > numRows - 1:
                li[numRows - j - 2].append(s[i])
            else:
                li[j].append(s[i])

        return ''.join(''.join(v) for v in li)
