class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(i)) + '#' + i for i in strs])


    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while j < len(s):
            while s[j] != '#':
                j += 1
            length = s[i:j]
            word = s[j+1:j+1+int(length)]
            res.append(word)
            j = j + 1 + int(length)
            i = j
        return res

        