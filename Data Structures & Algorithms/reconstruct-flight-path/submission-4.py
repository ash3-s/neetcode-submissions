class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()

        for src, dest in tickets:
            adj[src].append(dest)
        
        res = ["JFK"]
        def dfs(src):
            if len(tickets) + 1 == len(res):
                return True
            
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, dest in enumerate(temp):
                res.append(dest)
                adj[src].pop(i)

                if dfs(dest): return True

                res.pop()
                adj[src].insert(i, dest)
            # return False
        dfs("JFK")
        return res
            