class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        res = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashmap[tuple(count)].append(s)
        
        for i in hashmap.values():
            res.append(i)
        return res


