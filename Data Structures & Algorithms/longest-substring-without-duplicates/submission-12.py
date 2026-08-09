class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in hashmap and hashmap[s[r]] >= 1:
                hashmap[s[l]] -= 1
                l += 1
            hashmap[s[r]] += 1
            length = r - l + 1
            maxLen = max(maxLen, length)
        return maxLen
            
               