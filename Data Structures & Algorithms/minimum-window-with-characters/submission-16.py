class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        count = defaultdict(int)

        for c in t:
            count[c] += 1
        l = 0
        window = defaultdict(int)
        have, need = 0, len(count)
        minLen = float("inf")
        values = [-1, -1]
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in count and count[s[r]] == window[s[r]]:
                # if count[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                print(s[l:r+1])
                while l <= r and have == need:
                    print(s[l:r+1])
                    print(s[l] in count)
                    window[s[l]] -= 1
                    print(s[l] in count and window[s[l]] != count[s[l]])
                    if s[l] in count and window[s[l]] < count[s[l]]:
                        have -= 1
                    if r-l+1 < minLen:
                        minLen = r-l+1
                        values = [l,r]
                    l += 1
        l, r = values
        return s[l: r + 1] if minLen != float("inf") else ""
                
                


