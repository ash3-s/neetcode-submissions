class Solution:
    def isPalindrome(self, s: str) -> bool:
        return ''.join(c for c in  ''.join(s.lower().split()) if c.isalnum()) == ''.join(c for c in  ''.join(s.lower().split()) if c.isalnum())[::-1]