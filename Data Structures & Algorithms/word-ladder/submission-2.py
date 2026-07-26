class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        def differ_by_one(s1,s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        graph = {}
        begin_index = -1
        end_index = -1
        for i, s1 in enumerate(wordList):
            if not i in graph:
                graph[i] = set()
            
            if s1 == beginWord:
                begin_index = i
            if s1 == endWord:
                end_index = i
            
            for j,s2 in enumerate(wordList):
                if not j in graph:
                    graph[j] = set()

                if differ_by_one(s1, s2):
                    graph[i].add(j)
                    graph[j].add(i)
        
        if begin_index < 0 or end_index < 0 or beginWord == endWord:
            print(f"begin_index {begin_index} end_index: {end_index}")
            return 0
        
        length = 0
        queue = deque()
        visited = set()
        queue.append(begin_index)
        visited.add(begin_index)

        print(f"going {beginWord}({begin_index}) -> {endWord}({end_index})")
        print(f"wordList: {wordList}")
        print(f"graph: {graph}")

        while queue:
            length += 1
            for _ in range(len(queue)):
                element = queue.popleft()
                

                if element == end_index:
                    return length
                
                for child in graph[element]:
                    if not child in visited:
                        queue.append(child)
                        visited.add(child)
        
        return 0


        