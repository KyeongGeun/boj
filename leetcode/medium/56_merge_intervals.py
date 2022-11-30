class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l, r = intervals[0][0], intervals[0][1]

        ans = []
        for a, b in intervals:
            if a <= r:
                r = max(r, b)
            else:
                ans.append([l, r])
                l, r = a, b

        ans.append([l, r])

        return ans
