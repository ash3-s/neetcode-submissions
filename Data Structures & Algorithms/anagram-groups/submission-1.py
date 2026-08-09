class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        countdict = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for s in i:
                count[ord(s) - ord('a')] +=1
            countdict[tuple(count)].append(i)
        
        for k,v in countdict.items():
            res.append(v)
        return res
