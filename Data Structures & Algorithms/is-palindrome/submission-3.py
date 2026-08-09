class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join([i for i in "".join(s.lower().split()) if i.isalnum()]) == "".join([i for i in "".join(s.lower().split()) if i.isalnum()])[::-1]