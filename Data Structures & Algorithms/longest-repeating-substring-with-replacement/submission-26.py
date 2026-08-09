class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = defaultdict(int)
        maxLen = 0
        maxFreq = 0
        for r in range(len(s)):
            hashmap[s[r]] += 1
            if hashmap[s[r]] > maxFreq:
                maxFreq = hashmap[s[r]]
            if (r-l+1) - maxFreq > k:
                hashmap[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r-l+1)

        return maxLen