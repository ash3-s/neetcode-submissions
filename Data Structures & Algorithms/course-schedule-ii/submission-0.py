class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = { c:[] for c in range(numCourses) }

        for crs, pre in prerequisites:
            preReq[crs].append(pre)
        
        visit = set()
        cycle = set()
        output = []

        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for course in preReq[crs]:
                if not dfs(course): return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True           



        for c in range(numCourses):
            if not dfs(c): return []
        
        return output