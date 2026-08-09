class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        

        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False

            path.remove(src)
            order.append(src)
            return True

        def topoSort(edges):
            adj = defaultdict(list)
            for src, dest in edges:
                adj[src].append(dest)
            
            visit, path = set(), set()
            order = []
            for src in range(1, k + 1):
                if not dfs(src, adj, visit, path, order):
                    return []
            return order[::-1]        

        rowOrder = topoSort(rowConditions)
        colOrder = topoSort(colConditions)

        if not rowOrder or not colOrder:
            return []

        valToRow = { n:i for i, n in enumerate(rowOrder) }
        valToCol = { n:i for i, n in enumerate(colOrder) }

        matrix = [[0] * k for i in range(k)]
        for num in range(1, k + 1):
            r, c =  valToRow[num], valToCol[num]
            matrix[r][c] = num
        return matrix
