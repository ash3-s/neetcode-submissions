class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        return "".join(j for i in s.lower().split() for j in i if j.isalnum()) == "".join(j for i in s[::-1].lower().split() for j in i if j.isalnum())