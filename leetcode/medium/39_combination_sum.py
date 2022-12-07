class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        li = []

        def recur(idx=0, cur=0):
            if cur > target:
                return
            if cur == target:
                ans.append(li[:])

            for i in range(idx, len(candidates)):
                li.append(candidates[i])
                recur(i, cur + candidates[i])
                li.pop()

        recur()
        return ans
