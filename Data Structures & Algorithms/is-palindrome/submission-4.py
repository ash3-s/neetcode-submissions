class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s) - 1
        string = "".join([i for i in "".join(s.lower().split()) if i.isalnum()])
        return string == string[::-1]

        # while l < r:
        #     if l 