class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = 1 << 31

        for v in nums:
            if a >= v:
                a = v
            elif b >= v:
                b = v
            else:
                return True

        return False
