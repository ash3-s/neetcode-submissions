class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        l, r = 0, 0

        maxf = 0
        res = 0
        while r < len(s):
            hashmap[s[r]] += 1
            maxf = max(maxf,hashmap[s[r]])
            if (r-l+1) - maxf <= k:
                res = max(res, r-l+ 1) 
            else:
                while (r-l+1) - maxf > k:
                    hashmap[s[l]] -= 1 
                    l += 1 
            r += 1
        return res

            
