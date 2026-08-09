class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        res = ""
        maxLength = 1

        if len(s) == 0: return 0
        if len(s) == 1: return 1

        hashset = set() 
        while r < len(s):
            if s[r] not in hashset:
                maxLength = max(maxLength,len(s[l:r + 1]))

            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1 
            hashset.add(s[r])
            r += 1
        return maxLength

