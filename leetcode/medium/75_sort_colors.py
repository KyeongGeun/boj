class Solution:
    def sortColors(self, nums: List[int]) -> None:
        li = [0, 0, 0]

        while nums:
            li[nums.pop()] += 1

        for i in range(3):
            nums.extend([i] * li[i])
