class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        l = 0
        longest = 0
        for r in range(len(s)):
            hashmap[s[r]] += 1
            if (r-l+1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        return longest
                
            