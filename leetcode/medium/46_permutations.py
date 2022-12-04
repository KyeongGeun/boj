class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recur(cur=[], bit=0):
            if bit == ((1 << len(nums)) - 1):
                ans.append(cur[:])
                return

            for i in range(len(nums)):
                if not bit & (1 << i):
                    cur.append(nums[i])
                    recur(cur, bit | (1 << i))
                    cur.pop()

        recur()

        return ans
