class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(i)) + "#" + i for i in strs)

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        res = []
        while r < len(s):
            while s[r] != "#":
                r += 1
            length = s[l:r]
            word = s[r+1:r+1+int(length)]
            res.append(word)
            r = r + 1 + int(length)
            l = r
        return res

        