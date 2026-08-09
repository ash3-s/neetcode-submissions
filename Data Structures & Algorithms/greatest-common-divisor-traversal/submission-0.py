class UnionFind:
    def  __init__(self, n):
        self.par = [ i for i in range(n) ]
        self.rank = [1] * n
        self.count = n
    
    def find(self, n1):
        while n1 != self.par[n1]:
            n1 = self.par[self.par[n1]]
        return n1
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factorIndex = {}
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factorIndex:
                        uf.union(i, factorIndex[f])   
                    else:
                        factorIndex[f] = i
                while n % f == 0:
                    n = n // f 
                f += 1
            
            if n > 1:
                if n in factorIndex:
                    uf.union(factorIndex[n], i)
                else:
                    factorIndex[n] = i
        return uf.count == 1