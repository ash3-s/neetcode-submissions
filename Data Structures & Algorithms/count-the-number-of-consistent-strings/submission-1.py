class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashmap = defaultdict(int)

        for c in allowed:
            hashmap[c] += 1
        
        numbers = 0
        for w in words:
            worddict = defaultdict(int)
            matches = 0
            flag = True
            for c in w:
                worddict[c] += 1
                if c not in hashmap:
                    flag = False
                    break
                
            if flag:
                numbers += 1
        return numbers 

