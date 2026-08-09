class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts, countt = defaultdict(int), defaultdict(int)
        for i in s:
            counts[i] += 1
        for j in t:
            countt[j] += 1
        return counts == countt