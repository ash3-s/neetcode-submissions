class UnionFind:
    def  __init__(self, n):
        self.par = [ i for i in range(n) ]
        self.rank = [1] * n
    
    def find(self, n1):
        while n1 != self.par[n1]:
            n1 = self.par[self.par[n1]]
            
        return n1
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for i, e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda e: e[2])

        mstWeight = 0
        uf = UnionFind(n)
        for n1, n2, w, originalIndex in edges:
            if uf.union(n1, n2):
                mstWeight += w
        
        critical, pseudo = [], []
        for n1, n2, w, originalIndex in edges:
            uf = UnionFind(n)
            weight = 0
            for v1, v2, w2, j in edges:
                if originalIndex != j and uf.union(v1, v2):
                    weight += w2
            if max(uf.rank) != n or weight > mstWeight:
                critical.append(originalIndex)
                continue
            
            # include current edge
            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = w
            for v1, v2, w2, j in edges:
                if uf.union(v1, v2):
                    weight += w2
            if weight == mstWeight:
                pseudo.append(originalIndex)
        return [critical, pseudo]



