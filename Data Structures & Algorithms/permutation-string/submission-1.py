class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        have = [0 for i in range(26)]
        need = [0 for i in range(26)]

        for i in range(len(s1)):
            need[ord(s1[i])-ord("a")] += 1

        l, r = 0, 0
        while r < len(s2):
            have[ord(s2[r])-ord("a")] += 1
            if have == need:
                return True
            if r-l+ 1 == len(s1):
                have[ord(s2[l])-ord("a")] -= 1
                l += 1

            r += 1
        return False