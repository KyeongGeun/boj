class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            sortedStr = ''.join(sorted(list(s)))
            dic.setdefault(sortedStr, [])
            dic[sortedStr].append(s)

        return dic.values()
