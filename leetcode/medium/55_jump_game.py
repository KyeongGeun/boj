class Solution:
    def recur(self, cur, nums, visited):
        if cur >= len(nums) - 1:
            return True
        visited[cur] = True

        for i in range(min(len(nums) - 1, cur + nums[cur]), cur, -1):
            if visited[i]:
                continue
            if self.recur(i, nums, visited):
                return True

        return False

    def canJump(self, nums: List[int]) -> bool:
        visited = [False] * len(nums)

        if len(nums) == 1:
            return True

        return self.recur(0, nums, visited)
