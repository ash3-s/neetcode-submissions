class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = defaultdict(int)
        maxLen = 0
        for r in range(len(s)):
            hashmap[s[r]] += 1
            if (r-l+1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            # print(s[l:r+ 1])
            # print(max(hashmap.values()))
            # print((r-l+1))
            # print((r-l+1) - max(hashmap.values()))
            maxLen = max(maxLen, r-l+1)

        return maxLen