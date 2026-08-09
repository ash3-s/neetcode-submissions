class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + '#'+ s for s in strs)

    def decode(self, s: str) -> List[str]:
        i,j = 0,0
        res = []
        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + length +1
            j = i
        return res
