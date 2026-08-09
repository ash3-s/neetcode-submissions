class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(x)) + "#" + x for x in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find('#', i)
            length = s[i:j]
            w = s[j+1:j+1+int(length)]
            res.append(w)
            i = j+1+int(length)
        return res