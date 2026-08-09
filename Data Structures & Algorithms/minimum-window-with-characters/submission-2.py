class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        if t == "": return "" 

        res, resLen = [-1,-1], float("infinity")
        hashmap = {}
        window = {}

        matches = 0
        for i in range(len(t)):
            hashmap[t[i]] = 1 + hashmap.get(t[i],0)
        
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in hashmap and window[s[r]] == hashmap[s[r]]:
                matches += 1
            while matches == len(hashmap):
                if r-l+1 < resLen:
                    resLen = (r-l+1)
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in hashmap and window[s[l]] < hashmap[s[l]]:
                    matches -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""











        

