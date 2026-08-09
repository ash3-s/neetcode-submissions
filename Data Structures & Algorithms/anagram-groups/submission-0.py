class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        ddict = defaultdict(list)
        for i in strs:
            arr = 26 * [0]
            for c in i:
                arr[ord(c)-ord('a')] += 1
            ddict[tuple(arr)].append(i)
        for k,v in ddict.items():
            res.append(v)
        return res