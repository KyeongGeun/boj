class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def left():
            l, r = 0, len(nums) - 1

            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid

            if nums[l] != target:
                return -1
            return l

        def right():
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            if nums[l - 1] != target:
                return -1
            return l - 1

        return [left(), right()]
