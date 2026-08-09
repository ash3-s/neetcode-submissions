class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts, countt = {}, {}

        for i in s:
            counts[i] = 1 + counts.get(i,0)

        for i in t:
            countt[i] = 1 + countt.get(i,0)
        
        return counts == countt