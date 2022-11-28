class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for v in nums:
            dic.setdefault(v, 0)
            dic[v] += 1

        return list(map(lambda x: x[0], sorted(dic.items(), key=lambda x: -x[1])[:k]))
