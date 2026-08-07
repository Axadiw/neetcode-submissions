class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        for from_i,to_i in tickets:
            graph[from_i].append(to_i)
            graph[from_i] = deque(sorted(graph[from_i]))

        res = []
        def dfs(current):
            while graph[current]:
                ticket = graph[current].popleft()                
                dfs(ticket)            
            res.append(current)

        dfs("JFK")

        return res[::-1]