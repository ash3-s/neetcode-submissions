class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)

        for c in t:
            countT[c] += 1

        have, need = 0, len(countT)
        l = 0
        window = defaultdict(int)
        minLen, values = float("inf"), [-1, -1]
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                if r-l+1 < minLen:
                    values = [l, r]
                    minLen = r-l+1
                l += 1
        l, r = values
        return s[l:r+1] if minLen != float("inf") else "" 
            
