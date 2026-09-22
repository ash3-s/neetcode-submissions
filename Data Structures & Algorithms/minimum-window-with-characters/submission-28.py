class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]

        window = defaultdict(int)
        countT = defaultdict(int)

        for c in t:
            countT[c] += 1
        resLen = float("inf")
        have, need = 0, len(countT)


        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            
        
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                window[s[l]] -= 1
                if (r - l) + 1 < resLen:
                    res = [l, r]
                    resLen = (r - l) + 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""
