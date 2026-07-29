class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for s,dst,weight in edges:
            graph[s].append((weight,dst))
        
        ret_val = {}

        heap = [(0,src)]
        print(f"initial heap {heap}")
        print(graph)

        while heap:
            item = heapq.heappop(heap)
            if item[1] in ret_val:
                continue

            ret_val[item[1]] = item[0]
            print(f"item: {item} graph[item[1]: {graph[item[1]]}")
            for new_item in graph[item[1]]:
                print(f"new_item {new_item}")
                if new_item[1] not in ret_val:
                    heapq.heappush(heap, (new_item[0] + item[0],new_item[1]))

        for i in range(n):
            if i not in ret_val:
                ret_val[i] = -1
        return ret_val

