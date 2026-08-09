class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        su = list(s)
        for i in range(len(s)):
            slist = list(s)
            slist.pop(i)
            if "".join(slist) == "".join(slist)[::-1]:
                return True
        return False
