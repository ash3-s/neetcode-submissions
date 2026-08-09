class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts, countt = defaultdict(int), defaultdict(int)
        for i in s:
            counts[ord(i) - ord('a')] += 1
        for j in t:
            countt[ord(j) - ord('a')] += 1
        return counts == countt