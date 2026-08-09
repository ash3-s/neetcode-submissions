class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()

        adj = { i:[] for i in range(n) }
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        res = 0
        def dfs(node):
            if node in visit:
                return False
            
            visit.add(node)
            for a in adj[node]:
                dfs(a)
            return True
            
        for i in range(n):
            s = dfs(i)
            if s:
                res += 1
        return res