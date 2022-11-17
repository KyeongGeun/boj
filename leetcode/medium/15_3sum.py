class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cnt = 1
        temp = [nums[0]]
        for v in nums[1:]:
            if v == temp[-1]:
                if cnt > 2:
                    continue
                cnt += 1
            else:
                cnt = 1
            temp.append(v)

        nums = temp
        n = len(nums)
        nums.sort()
        ans = []

        sset = set()

        dic = {}
        for i, v in enumerate(nums):
            dic[v] = i

        for i in range(n):
            for j in range(i + 1, n):
                num = nums[i] + nums[j]
                third = -num

                s = ','.join(map(str, (nums[i], nums[j], third)))
                if s in sset:
                    continue
                sset.add(s)

                if third not in dic:
                    continue

                if dic[third] > j:
                    ans.append((nums[i], nums[j], third))

        return ans
