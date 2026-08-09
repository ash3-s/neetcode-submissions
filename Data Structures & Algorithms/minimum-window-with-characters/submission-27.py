class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = defaultdict(int), defaultdict(int)
        string = ""
        for c in t:
            countT[c] += 1
        
        l = 0
        matched = 0
        minLen = float("inf")
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                matched += 1
            while matched == len(countT):
                window[s[l]] -= 1
                # print(string)
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    matched -= 1
                if r-l+1 < minLen:
                    minLen = r-l+1
                    string = s[l:r+1]
                l += 1
        return string
