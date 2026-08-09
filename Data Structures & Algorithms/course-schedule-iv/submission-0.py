class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = { i:[] for i in range(numCourses) }

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        preReqMap = defaultdict(set)
        def dfs(crs):
            if crs not in preReqMap:
                for p in adj[crs]:
                    preReqMap[crs] |= (dfs(p))
                preReqMap[crs].add(crs)
            return preReqMap[crs]
            

        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in preReqMap[v])
        
        return res
